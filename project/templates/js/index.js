//document.getElementById('#menu-home"').focus();

/* Tab
    -------------------------------------- */
$('.tab-content>div').hide();
$('.tab-content>div').first().slideDown();
$('.tab-buttons span').click(function () {
    var thisclass = $(this).attr('class');
    $('#lamp').removeClass().addClass('#lamp').addClass(thisclass);
    $('.tab-content>div').each(function () {
        if ($(this).hasClass(thisclass)) {
            $(this).fadeIn(800);
        }
        else {
            $(this).hide();
        }
    });
    //tabの文字にcurrentを付与して青くする
    $('.tab-buttons span').each(function () {
        if ($(this).hasClass(thisclass)) {
            $(this).addClass('tab-current');
        } else {
            $(this).removeClass('tab-current');
        }
    });
});


/* Search Field
    -------------------------------------- */
$(function () {
    // 検索フィールドフォーカス時にフォームの縁の色を変える
    $('#search-input')
        .focusin(function (e) {
            $('#search-form').addClass('form-focused');
        })
        .focusout(function (e) {
            $('#search-form').removeClass('form-focused');
        });
    // パスワードフィールドフォーカス時にフォームの縁の色を変える
    $('#password')
        .focusin(function (e) {
            $('.pw-input-container').addClass('form-focused');
        })
        .focusout(function (e) {
            $('.pw-input-container').removeClass('form-focused');
        });


    /* // 検索フィールドエラー時にフォームの縁の色を変える ざっと探したけどfocusInvalidって間違っている模様（エラー出てる）直したいけど優先しなくていい
     $('#search-input')
         .focusInvalid(function (e) {
             $('#search-form').addClass('form-error');
         })
         .fvalid(function (e) {
             $('#search-form').removeClass('form-error');
         });
     // パスワードフィールドエラー時にフォームの縁の色を変える
     $('#password')
         .focusInvalid(function (e) {
             $('.pw-input-container').addClass('form-error');
         })
         .valid(function (e) {
             $('.pw-input-container').removeClass('form-error');
         });*/
});



/* Password
    -------------------------------------- */
const visibilityToggle = document.querySelector('.visibility');

const input = document.querySelector('.input-container input');

var password = true;

visibilityToggle.addEventListener('click', function () {
    if (password) {
        input.setAttribute('type', 'text');
        visibilityToggle.innerHTML = 'visibility';
    } else {
        input.setAttribute('type', 'password');
        visibilityToggle.innerHTML = 'visibility_off';
    }
    password = !password;

});


/* URL Copy Button
    -------------------------------------- */
function copyUrl() {
    const element = document.createElement('input');
    element.value = location.href;
    document.body.appendChild(element);
    element.select();
    document.execCommand('copy');
    document.body.removeChild(element);
}
/* Share Button
    -------------------------------------- */
if (navigator.share !== undefined) {
    /* 未対応ブラウザも多いので判定処理 */
    document.addEventListener('DOMContentLoaded', () => {
        for (const shareButtonElement of document.querySelectorAll('.native-share-btn')) {
            //shareButtonElement.disabled = false; // ボタンを活性化
            shareButtonElement.addEventListener('click', () => {
                const shareTitle = shareButtonElement.dataset.shareTitle;
                const shareText = shareButtonElement.dataset.shareText;
                const shareUrl = shareButtonElement.dataset.shareUrl;

                try {
                    navigator.share({
                        title: shareTitle !== undefined ? shareTitle : document.title, // 属性が指定されていないときはページタイトル
                        text: shareText,
                        url: shareUrl !== undefined ? shareUrl : document.URL, // 属性が指定されていないときはページURL
                    });
                } catch (e) {
                    console.error('Share failed', e);
                }
            });
        }
    });
}


var body = document.body;

var checkbox = document.getElementsByClassName('modalCheck');

for (var i = 0; i < checkbox.length; i++) {

    checkbox[i].addEventListener('click', function () {

        if (this.checked) {

            body.style.overflow = 'hidden';

        } else {

            body.style.overflow = 'visible';

        }

    });

}
