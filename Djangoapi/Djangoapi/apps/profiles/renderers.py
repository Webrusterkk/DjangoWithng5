from Djangoapi.apps.core.renderers import APIJSONRenderer


class ProfileJSONRenderer(APIJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
