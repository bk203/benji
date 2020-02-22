# General labels
LABEL_INSTANCE = 'benji-backup.me/instance'
LABEL_K8S_PVC_NAMESPACE = 'benji-backup.me/k8s-pvc-namespace'
LABEL_K8S_PVC_NAME = 'benji-backup.me/k8s-pvc-name'
LABEL_K8S_PV_NAME = 'benji-backup.me/k8s-pv-name'
LABEL_K8S_STORAGE_CLASS_NAME = 'benji-backup.me/k8s-storage-class-name'
LABEL_K8S_PV_TYPE = 'benji-backup.me/k8s-pv-type'

# RBD specific
LABEL_RBD_CLUSTER_FSID = 'benji-backup.me/rbd-cluster-fsid'
LABEL_RBD_IMAGE_SPEC = 'benji-backup.me/rbd-image-spec'

# PV types
PV_TYPE_RBD = 'rbd'

# Key names in version
VERSION_UID = 'uid'
VERSION_DATE = 'date'
VERSION_VOLUME = 'volume'
VERSION_SNAPSHOT = 'snapshot'
VERSION_SIZE = 'size'
VERSION_STORAGE = 'storage'
VERSION_BYTES_READ = 'bytes_read'
VERSION_BYTES_WRITTEN = 'bytes_written'
VERSION_BYTES_DEDUPLICATED = 'bytes_deduplicated'
VERSION_BYTES_SPARSE = 'bytes_sparse'
VERSION_DURATION = 'duration'
VERSION_PROTECTED = 'protected'
VERSION_STATUS = 'status'
VERSION_LABELS = 'labels'

# Names used in version resource
RESOURCE_SPEC_DATE = 'date'
RESOURCE_SPEC_VOLUME = 'volume'
RESOURCE_SPEC_SNAPSHOT = 'snapshot'
RESOURCE_SPEC_SIZE = 'size'
RESOURCE_SPEC_STORAGE = 'storage'
RESOURCE_SPEC_BYTES_READ = 'bytesRead'
RESOURCE_SPEC_BYTES_WRITTEN = 'bytesWritten'
RESOURCE_SPEC_BYTES_DEDUPLICATED = 'bytesDeduplicated'
RESOURCE_SPEC_BYTES_SPARSE = 'bytesSparse'
RESOURCE_SPEC_DURATION = 'duration'
RESOURCE_SPEC_VOLUME_INFO = 'volumeInfo'
RESOURCE_SPEC_VOLUME_INFO_PERSISTENT_VOLUME_NAME = 'persistentVolumeName'
RESOURCE_SPEC_VOLUME_INFO_PERSISTENT_VOLUME_CLAIM_NAME = 'persistentVolumeClaimName'
RESOURCE_SPEC_VOLUME_INFO_STORAGE_CLASS_NAME = 'storageClassName'

RESOURCE_SPEC_VOLUME_INFO_RBD_CLUSTER_FSID = 'clusterFSID'
RESOURCE_SPEC_VOLUME_INFO_RBD_IMAGE_SPEC = 'imageSpec'

RESOURCE_STATUS_PROTECTED = 'protected'
RESOURCE_STATUS_STATUS = 'status'
