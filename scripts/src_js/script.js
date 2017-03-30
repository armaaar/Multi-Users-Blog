jQuery(function($){

    $(document).ready(function(){
        // Replace the <textarea id="editor"> with a CKEditor
        // instance, using default configuration.
        if($("#editor").length != 0) {
            CKEDITOR.replace( 'editor' );
        }
    });
});
