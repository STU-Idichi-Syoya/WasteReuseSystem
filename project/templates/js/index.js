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

function postComment() {
    //コメントの送信　できなくてもいいので一旦パス
}



/*--------------------------------------------------------------
#アイテムの情報に関わる関数（主にモーダル関連）
--------------------------------------------------------------*/
/* 投稿
-------------------------------------- */
function savePost() {
    //下書きに保存(パス)

}

function checkDeletePost() {
    //投稿画面「削除する」で下書き消すか確認モーダルを開く
    $('.modal-wrapper.check-delete').fadeIn();

}
function deletePost() {
    //投稿画面「削除する」で下書き消すか確認モーダルを閉じる
    $('.modal-wrapper.check-delete').fadeOut().css({ top: 0 });
    //下書き削除(パス)
    //下書き一覧に飛ばす
}
function checkPost() {
    //投稿するボタンで確認モーダルを開く

    let howDelivery = $('#input-how-delivery').value;//undefined
    console.log(howDelivery);
    //取引画面「受け渡しに進む」ボタンを押したら
    if (howDelivery == '置いておく') {//受け渡し方法が「置いておく」の場合
        //投稿確認（置いておく）モーダルを開く
        $('.modal-wrapper.check-post.leave').fadeIn();
        return false;
    } else {//受け渡し方法が「手渡し」の場合
        //投稿確認（手渡し）モーダルを開く
        $('.modal-wrapper.check-post.hand').fadeIn();
    }


}

function postItem() {
    //投稿確認モーダルを閉じる
    $('.modal-wrapper.check-post').fadeOut().css({ top: 0 });
    //投稿する
}

/* 取引
-------------------------------------- */
function checkConditions() {
    let howDelivery = $('#disp-how-delivery').value;//undefined
    console.log(howDelivery);
    //アイテム詳細「もらい手になる」ボタンを押したら取引開始確定前のチェックモーダルに飛ばす
    if (howDelivery == '置いておく') {//受け渡し方法が「置いておく」の場合
        //受け渡し（置いておく）モーダルを開く
        $('.modal-wrapper.check-conditions.leave').fadeIn();
        return false;

    } else {//受け渡し方法が「手渡し」の場合
        $('.modal-wrapper.check-conditions.hand').fadeIn();
        return false;
    }
}


function gotoTransaction() {
    //取引開始確認モーダルの「確定する」ボタンを押したら
    //確認モーダルを非表示
    $('.modal-wrapper.check-conditions').fadeOut().css({ top: 0 });
    //取引ページに飛ぶ
    return false;
}

function gotoDelivery() {
    let howDelivery = '手渡し'//受け渡し方法、本当はどこかからとってくる
    let role = "もらい手"//ユーザーの役割、本当はどこかからとってくる
    //取引画面「受け渡しに進む」ボタンを押したら
    if (howDelivery == '置いておく') {//受け渡し方法が「置いておく」の場合
        //受け渡し（置いておく）モーダルを開く
        $('.modal-wrapper.delivey.leave').fadeIn();
        return false;
    } else {//受け渡し方法が「手渡し」の場合
        if (role == '投稿者') {//役割が投稿者の場合
            $('.modal-wrapper.delivey.hand.contributor').fadeIn();
            return false;
        } else {//役割がもらい手の場合
            $('.modal-wrapper.delivey.hand.recipient').fadeIn();
            return false;
        }
    }
}
/* 取引
-------------------------------------- */
function cancelTransaction() {
    /*取引画面「取引をキャンセルする」ボタンを押したら取引キャンセル画面に遷移する */
    $('.modal-wrapper.cancel-transaction').fadeIn();
    return false;
}

function endCancel() {
    //キャンセルメッセージを「送信する」ボタンをを押したら、
    //キャンセル理由とメッセージの取得
    let whyCancel = $('#why-cancel').value
    let canselMsg = $('#cansel-msg').value
    console.log(whyCancel, canselMsg);//なぜかundefined、わからない、ほっとく
    //取引キャンセル用モーダルを表示オフ
    $('.modal-wrapper.cancel-transaction').fadeOut().css({ top: 0 });
    return false;

}

/* 受け渡し〜評価
-------------------------------------- */
function noItem() {
    /*初めは隠してあるヘルプコンテンツの表示 */
    $('.modal-contents .bg-color').css('display', 'block');
}

function gotoEvaluation() {
    //「受け取りました！」ボタンをを押したら、取引用モーダルを表示オフしてから評価用のモーダルを表示
    $('.modal-wrapper.delivey').fadeOut().css({ top: 0 });
    $('.modal-wrapper.evaluation').fadeIn();
    return false;
    /*受け渡し（取引）完了の送信 */
}
function submitEvaluation() {
    //評価モーダルを閉じる
    $('.modal-wrapper.evaluation').fadeOut().css({ top: 0 });
    return false;
    //評価の送信
    //チェックされてるラジオボタンの値を取ればいいと思うけどパス

}
function endTransaction() {
    //「このまま取引を終わる」ボタンをを押したら、取引用モーダルを表示オフ
    $('.modal-wrapper.evaluation').fadeOut().css({ top: 0 });
    return false;
    //実質受け渡し（取引）完了の送信
}


// 閉じる用・moral_test.htmlで開くテスト用

$(function () {

    // 下書き削除モーダルの開閉）

    $('.modal-open.check-delete').click(function () {

        $('.modal-wrapper.check-delete').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.check-delete').click(function () {
        $('.modal-wrapper.check-delete').fadeOut().css({ top: 0 });
        return false;
    });
    // 投稿確認モーダルの開閉（置いておく）

    $('.modal-open.check-post.leave').click(function () {

        $('.modal-wrapper.check-post.leave').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.check-post.leave').click(function () {
        $('.modal-wrapper.check-post.leave').fadeOut().css({ top: 0 });
        return false;
    });

    // 投稿確認モーダルの開閉（手渡し）

    $('.modal-open.check-post.hand').click(function () {

        $('.modal-wrapper.check-post.hand').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.check-post.hand').click(function () {
        $('.modal-wrapper.check-post.hand').fadeOut().css({ top: 0 });
        return false;
    });


    // 取引開始確認モーダルの開閉（置いておく）

    $('.modal-open.check-conditions.leave').click(function () {

        $('.modal-wrapper.check-conditions.leave').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.check-conditions.leave').click(function () {
        $('.modal-wrapper.check-conditions.leave').fadeOut().css({ top: 0 });
        return false;
    });

    // 取引開始確認モーダルの開閉（手渡し）

    $('.modal-open.check-conditions.hand').click(function () {

        $('.modal-wrapper.check-conditions.hand').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.check-conditions.hand').click(function () {
        $('.modal-wrapper.check-conditions.hand').fadeOut().css({ top: 0 });
        return false;
    });


    // 取引キャンセルモーダルの開閉

    $('.modal-open.cancel-transaction').click(function () {

        $('.modal-wrapper.cancel-transaction').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.cancel-transaction').click(function () {
        $('.modal-wrapper.cancel-transaction').fadeOut().css({ top: 0 });
        return false;
    });


    // 受け渡し（置いておく）モーダルの開閉

    $('.modal-open.delivey.leave').click(function () {

        $('.modal-wrapper.delivey.leave').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.delivey.leave').click(function () {
        $('.modal-wrapper.delivey.leave').fadeOut().css({ top: 0 });
        return false;
    });


    // 受け渡し（手渡し,もらい手）モーダルの開閉

    $('.modal-open.delivey.hand.recipient').click(function () {

        $('.modal-wrapper.delivey.hand.recipient').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.delivey.hand.recipient').click(function () {
        $('.modal-wrapper.delivey.hand.recipient').fadeOut().css({ top: 0 });
        return false;
    });

    // 受け渡し（手渡し,投稿者）モーダルの開閉

    $('.modal-open.delivey.hand.contributor').click(function () {

        $('.modal-wrapper.delivey.hand.contributor').fadeIn();
        return false;
    });
    $('.overlay, .modal-close.delivey.hand.contributor').click(function () {
        $('.modal-wrapper.delivey.hand.contributor').fadeOut().css({ top: 0 });
        return false;
    });



    //評価モーダルの開閉

    $('.modal-open.evaluation').click(function () {

        $('.modal-wrapper.evaluation').fadeIn();

        return false;
    });
    $('.overlay, .modal-close.evaluation').click(function () {
        $('.modal-wrapper.evaluation').fadeOut().css({ top: 0 });


        return false;
    });


});

