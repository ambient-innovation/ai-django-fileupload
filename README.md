# Overview:
This package provides an easy way to implement the [jQuery Fileuploader](https://github.com/blueimp/jQuery-File-Upload), in your Django project.

The uploaded files are stored through the Attachment model. Attachments could be linked to any model.

Additionally, a list of attachments is rendered along with the uploader button. These attachments have a convenient delete feature.  


# Installation:
- Add a requirement to your requirements.txt: 
    
    `ai-django-fileupload`

- Add module to `INSTALLED_APPS`:

    `fileupload.apps.FileuploadConfig`

- Add module's urls to your url file:

    `url(r'^upload/', include('fileupload.urls')),`
    
- Add static files. They are not included in this package, though a convenient [npm package](https://www.npmjs.com/package/ai-django-fileupload) is provided.  
    
    `npm install ai-django-fileupload`
   
- Run migrations

# Settings

## Default thumbnail image
The uploader comes with a default thumbnail image, in case it couldn't be generated. 

You can set your own one, adding its location to the settings file: 

    UPLOADER_DEFAULT_THUMBNAIL = '/static/img/default-thumbnail.png'
    
Otherwise it'd be fetched from "static/node_modules/ai-django-fileupload/img/default-thumbnail.png". You may find useful to copy this image wherever your static content is stored. 

## Login required
If your uploader needs the user be authenticated, you can enable this restriction adding this to the settings file:
    
    UPLOADER_LOGIN_REQUIRED = True
    
# Usage:
- Include the upload_file template tag in your template:

    `{% load upload_file %}`
    
- Call it with the object that the uploaded files will be attached to:

    `{% upload_file obj=object %}`
   
   Make sure to put the template tag outside any other form tags you have since it will render a new form.
   
- For a minimal setup, please load the following files. Scripts order is important.

```
  <link rel="stylesheet" type="text/css" href="node_modules/bootstrap/dist/css/bootstrap.min.css"/>
  <link rel="stylesheet" type="text/css" href="node_modules/blueimp-file-upload/css/jquery.fileupload.css">
  
  <!-- jQuery -->
  <script src="node_modules/jquery/dist/jquery.js"></script>
  
  <!-- The jQuery UI widget factory, can be omitted if jQuery UI is already included -->
  <script src="node_modules/blueimp-file-upload/js/vendor/jquery.ui.widget.js"></script>
  
  <!-- The Templates plugin is included to render the upload/download listings -->
  <script src="node_modules/blueimp-tmpl/js/tmpl.min.js"></script>
  
  <!-- The Load Image plugin is included for the preview images and image resizing functionality -->
  <script src="node_modules/blueimp-load-image/js/load-image.all.min.js"></script>
  
  <!-- The Canvas to Blob plugin is included for image resizing functionality -->
  <script src="node_modules/blueimp-canvas-to-blob/js/canvas-to-blob.min.js"></script>
  
  <!-- The basic File Upload plugin and components-->
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-process.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-image.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-audio.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-video.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-validate.js"></script>
  <script src="node_modules/blueimp-file-upload/js/jquery.fileupload-ui.js"></script>
  
  <!-- Locale -->
  <script src="node_modules/ai-django-fileupload/locale.js"></script>
  
  <!-- CSRF token -->
  <script src="node_modules/ai-django-fileupload/csrf.js"></script>
  
  <!-- The main application script -->
  <script src="node_modules/ai-django-fileupload/index.js"></script>
  
  <!-- The XDomainRequest Transport is included for cross-domain file deletion for IE8+ -->
  <!--[if gte IE 8]>
  <script src="node_modules/blueimp-file-upload/js/cors/jquery.xdr-transport.js"></script>
  <![endif]-->
```

# Contribute

- Clone the project locally
- Create a new branch for your feature
- Change the dependency in your requirements.txt to a local (editable) one that points to your local file system:
    ```
    -e /Users/felix/Documents/workspace/ai-django-fileupload
    ``` 
- Ensure the code passes the tests
- Run: 
    
    `python setup.py develop`
    
- Create a pull request

# Publish to PyPI

- Run:

    `python setup.py sdist upload`

# Tests
- Install requirements

    `pip install -r requirements.pip`

- Check coverage

    `pytest --cov=fileupload fileupload`
    
- Run tests

    `pytest`
