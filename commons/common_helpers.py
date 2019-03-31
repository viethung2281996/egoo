from egoo_core.cloudinary import CloudinaryUploader

class CommonHelper:
  model_class = object
  serializer_class = object

  @classmethod  
  def get_object(cls, object_id):
    try:
      obj = cls.model_class.objects.get(id=object_id)
    except ObjectDoesNotExist:
      return None
    return obj

  @classmethod
  def upload(cls, obj, file, folder, resource_type):
    file_name = obj.init_file_name(file)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder=folder, resource_type=resource_type)
    response = uploader.upload()
    return response['secure_url']

  @classmethod
  def update_data(cls, obj, data):
    serializer = cls.serializer_class(obj, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return serializer.data
    else:
      return None