// HTML要素取得
const txt = document.getElementById('txt');
const btn = document.getElementById('btn');

// コピー処理（btnがクリックされたらtxtをコピーする）
btn.addEventListener('click', () => {
    if (!navigator.clipboard) {
        alert("残念ですが、このブラウザは対応していません...");
        return;
    }

    navigator.clipboard.writeText(txt.textContent).then(
        () => {
            alert('リンクをクリップボードにコピーできました！\nメール本文などに貼り付けて利用できます。');
        },
        () => {
            alert('クリップボードにコピーできませんでした。');
        });
});
