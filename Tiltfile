analytics_settings(enable=False)
version_settings(check_updates=False)
disable_snapshots()
docker_prune_settings(disable=False, num_builds=1, max_age_mins=5)

config.define_string_list('vcs-ref')
config.define_string_list('build-date')
config.define_string_list('vcs-url')
config.define_string_list('version')
config.define_string_list('args', args=True)
cfg = config.parse()
config.set_enabled_resources(cfg.get('args', []))

allow_k8s_contexts('dev-context')

docker_build(
    'elementalnet/benji',
    '.',
    dockerfile='images/benji/Dockerfile',
    build_args={
        'VCS_REF': cfg.get('vcs-ref', 'unknown'),
        'BUILD_DATE': cfg.get('build-date', 'unknown'),
        'VCS_URL': cfg.get('vcs-url', 'unknown'),
        'VERSION': cfg.get('version', 'unknown'),
    },
    # Disable Live Update for the time being, see https://github.com/windmilleng/tilt/issues/2948.
    # live_update=[
    #     sync('src/benji', '/benji/lib/python3.6/site-packages/benji'),
    #     restart_container(),
    # ],
    ignore=['src/benji/k8s_operator', 'images', '!images/benji'])

docker_build(
    'elementalnet/benji-k8s',
    '.',
    dockerfile='images/benji-k8s/Dockerfile',
    build_args={
        'VCS_REF': cfg.get('vcs-ref', 'unknown'),
        'BUILD_DATE': cfg.get('build-date', 'unknown'),
        'VCS_URL': cfg.get('vcs-url', 'unknown'),
        'VERSION': cfg.get('version', 'unknown'),
    },
    # Disable Live Update for the time being, see https://github.com/windmilleng/tilt/issues/2948.
    # live_update=[
    #     sync('src/benji', '/benji/lib/python3.6/site-packages/benji'),
    #     restart_container(),
    # ],
    ignore=['src/benji/k8s_operator', 'images', '!images/benji-k8s'])

docker_build('elementalnet/benji-k8s-operator',
             '.',
             dockerfile='images/benji-k8s-operator/Dockerfile',
             build_args={
                 'VCS_REF': cfg.get('vcs-ref', 'unknown'),
                 'BUILD_DATE': cfg.get('build-date', 'unknown'),
                 'VCS_URL': cfg.get('vcs-url', 'unknown'),
                 'VERSION': cfg.get('version', 'unknown'),
             },
             live_update=[
                 sync('src/benji', '/usr/local/lib/python3.7/site-packages/benji'),
                 restart_container(),
             ],
             ignore=['images', '!images/benji-k8s-operator'])

k8s_resource('benji-operator', resource_deps=['benji-api'])
k8s_resource('benji', extra_pod_selectors=[{'app.kubernetes.io/managed-by': 'benji-operator'}])

k8s_kind('BenjiOperatorConfig',
         image_json_path=[
             '{.spec.jobTemplate.spec.template.spec.containers[0].image}',
             '{.spec.cronJobTemplate.spec.jobTemplate.spec.template.spec.containers[0].image}'
         ])

# See https://github.com/windmilleng/tilt/issues/2805.
#
# helm('charts/benji-k8s',
#      namespace='ceph',
#      name='benji',
#      values=['../../dual/dual/addons/values/global/benji.yaml', '../../dual/dual/addons/values/dev/benji.yaml']))

helm_template = str(
    helm('charts/benji-k8s',
         namespace='ceph',
         name='benji',
         values=['../../dual/dual/addons/values/global/benji.yaml', '../../dual/dual/addons/values/dev/benji.yaml']))
helm_template = helm_template[helm_template.index('---'):]
k8s_yaml(blob(helm_template))
