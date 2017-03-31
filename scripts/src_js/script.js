jQuery(function($){

    $(document).ready(function(){
        // Replace the <textarea id="editor"> with a CKEditor
        // instance, using default configuration.
        if($("#editor").length != 0) {
            CKEDITOR.replace( 'editor' );
        }

        SocialShareKit.init();

        $(document).on("click","a.comment-edit", function(){
            comment_id = $(this).attr("data-id");
            state = $(this).attr("data-edit");
            $commentContainer = $("#comment-"+comment_id+" .comment-body")
            if(state == "0")
            {
                comment = $commentContainer.find(".actual-comment").hide().text();
                $commentContainer.find('textarea[name="comment"]').removeAttr("disabled").show().val(comment);
                $commentContainer.find('button[name="edit-comment"]').removeAttr("disabled").show();
                $(this).attr("data-edit", 1).text("Cancel");
            } else {
                $commentContainer.find(".actual-comment").show();
                $commentContainer.find('textarea[name="comment"]').attr("disabled", "disabled").hide().val("");
                $commentContainer.find('button[name="edit-comment"]').attr("disabled", "disabled").hide();
                $(this).attr("data-edit", 0).text("Edit");
            }

        });

    });
});
