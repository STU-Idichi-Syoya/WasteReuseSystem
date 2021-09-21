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

/* Search Bar Fix（あるところだけ）
    -------------------------------------- */
/*スクロールすると検索フィールドが上に固定される（実は微妙にうまく行ってない）*/
var startPos = 0, winScrollTop = 0;


$(window).on('scroll', function () {
    winScrollTop = $(this).scrollTop();
    if (winScrollTop >= startPos) {
        //下に行ってる時 top:0まで上げて固定する
        $('.head-fix').addClass('hide');

    } else {//上に行ってるとき
        // $('.head-fix').removeClass('hide');
        if (winScrollTop <= 60) {//headerの高さ以下までたどり着いたら元の位置に固定する
            $('.head-fix').removeClass('hide');
        }
    }
    startPos = winScrollTop;
});

/* Search Field
    -------------------------------------- */
$(function () {
    // 検索フィールドフォーカス時にフォームの縁の色を変える
    $('#search-input')
        .focusin(function (e) {
            $('#search-form').addClass('form-focused shrink');
            $('#search-back').addClass('visible');
            $('#search-input').attr('placeholder', 'キーワードで検索');
            //検索ページがフォーカス時に左から出てくる
            $('.searching').removeClass('off');
            $('.searching').animate({ 'marginLeft': '100vw' }, 400).addClass('on');

        })
        .focusout(function (e) {
            $('#search-form').removeClass('form-focused shrink');
            $('#search-back').removeClass('visible');
            $('#search-input').attr('placeholder', '何をお探しですか？');
            //検索ページがフォーカス外した時に左に消える
            $('.searching').addClass('off');
            $('.searching').animate({ 'marginLeft': '0px' }, 400);

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

//検索ページがbackを押した時に左に消える
$('#search-back').on('click', function () {
    $('.searching').addClass('off');
    $('.searching').animate({ 'marginLeft': '0px' }, 400);

});


/* Password（あるところだけ）
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

    $('.btn-like').click(function () {
        if ($(this).hasClass('liked')) {
            $(this).removeClass('liked');

        } else {
            $(this).addClass('liked');

        }

    })
});

/* Reaction Button（カウントは表示できてない）
    -------------------------------------- */

$(function () {

    $('.reactions>button').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');

        } else {
            $(this).addClass('active');

        }
    })

    $('.btn-good').click(function () {
        /*1つのコメントごとに別々のIDを付けないとカウントできない... */
        if ($(this).hasClass('active')) {
            let goodNum = parseInt(document.getElementById('good-num').innerText);
            document.getElementById('good-num').innerText = goodNum + 1;
        }
    })
    $('.btn-thanks').click(function () {
        /*1つのコメントごとに別々のIDを付けないとカウントできない... */
        if ($(this).hasClass('active')) {
            let thanksNum = parseInt(document.getElementById('thanks-num').innerText);
            document.getElementById('thanks-num').innerText = thanksNum + 1;
        }
    })
});

/* 投稿画面 撮影/選択済みの画像の削除 
   -------------------------------------- */
$(function () {
    $('.btn-delete').click(function () {
        //写真を消す

    })
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
/*--------------------------------------------------------------
#取引
--------------------------------------------------------------*/


function gotoDelivery() {
    /*「受け渡しに進む」ボタンクリックで受け渡しモーダルを開く */
}

function cancelTransaction() {
    /*「取引をキャンセルする」ボタンクリックで取引キャンセル画面に遷移する */
}
/*--------------------------------------------------------------
#modal window
--------------------------------------------------------------*/
/* 受け渡し
-------------------------------------- */
function noItem() {
    /*初めは隠してあるヘルプコンテンツの表示 */
    $('.modal-contents .bg-color').css('display', 'block');
}

function gotoEvaluation() {
    //「受け取りました！」ボタンをクリックで、取引用モーダルを表示オフしてから評価用のモーダルを表示
    $('.modal-wrapper.delivey-leave').fadeOut().css({ top: 0 });
    $('.modal-wrapper.evaluation').fadeIn();
    return false;
    /*受け渡し（取引）完了の送信 */
}
function submitEvaluation() {
    /*評価の送信*/
}
function endTransaction() {
    //「このまま取引を終わる」ボタンをクリックで、取引用モーダルを表示オフ
    $('.modal-wrapper.evaluation').fadeOut().css({ top: 0 });
    $('body').removeClass('fixed');
    $(window).scrollTop(scrollPos);
    return false;
    /*実質受け渡し（取引）完了の送信 */
}


/* テスト用
-------------------------------------- */
$(function () {
    /* 受け渡しモーダルの開閉
    -------------------------------------- */
    var scrollPos;
    $('.modal-open.delivey-leave').click(function () {
        scrollPos = $(window).scrollTop();
        $('.modal-wrapper.delivey-leave').fadeIn();
        $('body').addClass('fixed').css({ top: -scrollPos });
        return false;
    });
    $('.overlay, .modal-close.delivey-leave').click(function () {
        $('.modal-wrapper.delivey-leave').fadeOut().css({ top: 0 });
        $('body').removeClass('fixed');
        $(window).scrollTop(scrollPos);
        return false;
    });


    /* 評価モーダルの開閉
        -------------------------------------- */
    $('.modal-open.evaluation').click(function () {
        scrollPos = $(window).scrollTop();
        $('.modal-wrapper.evaluation').fadeIn();
        $('body').addClass('fixed').css({ top: -scrollPos });
        return false;
    });
    $('.overlay, .modal-close.evaluation').click(function () {
        $('.modal-wrapper.evaluation').fadeOut().css({ top: 0 });
        $('body').removeClass('fixed');
        $(window).scrollTop(scrollPos);
        return false;
    });


});

