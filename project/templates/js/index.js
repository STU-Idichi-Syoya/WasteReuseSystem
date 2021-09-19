
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


    // 検索フィールドエラー時にフォームの縁の色を変える
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
        });
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