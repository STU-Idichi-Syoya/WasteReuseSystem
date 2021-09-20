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
/*
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

});*/


/* Like Button
    -------------------------------------- */

$(function () {
    // 検索フィールドフォーカス時にフォームの縁の色を変える
    $('.btn-like').click(function () {
        if ($(this).hasClass('liked')) {
            $(this).removeClass('liked');
            console.log('likedはずされされました！');
        } else {
            $(this).addClass('liked');
            console.log('likedクリックされました！');
        }

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
/*

function getCheckedRadioId(){
    var flag = false; // 選択されているか否かを判定するフラグ

    //　ラジオボタンの数だけ判定を繰り返す（ボタンを表すインプットタグがあるので１引く）
    for(var i = 0 ; i < document.getElementsByName('radio').length  ; i++){
        // i番目のラジオボタンがチェックされているかを判定
        if(document.getElementsByName('radio')[i].checked){ 
            flag = true;
            return i+1;
        }
    }*/

/*
const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'vertical',
    loop: true,

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});*/
/*

var mySwiper = new Swiper(".swiper-container", {
    // オプション設定
    loop: true, // ループ
    speed: 600, // 切り替えスピード(ミリ秒)。
    slidesPerView: 1, // １スライドの表示数
    spaceBetween: 0, // スライドの余白(px)
    direction: "horizontal", // スライド方向
    effect: "fade", // スライド効果 ※ここを変更

    // スライダーの自動再生設定
    autoplay: {
        delay: 3000, // スライドが切り替わるまでの時間(ミリ秒)
        stopOnLast: false, // 自動再生の停止なし
        disableOnInteraction: true, // ユーザー操作後の自動再生停止
    },

    // ページネーションを有効化
    pagination: {
        el: ".swiper-pagination",
    },

    // ナビゲーションを有効化
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
*/
var startPos = 0, winScrollTop = 0;


$(window).on('scroll', function () {
    winScrollTop = $(this).scrollTop();
    if (winScrollTop >= startPos) {

        $('.head-fix').addClass('hide');
        if (winScrollTop <= 60) {

        }
    } else {
        $('.head-fix').removeClass('hide');
    }
    startPos = winScrollTop;
});