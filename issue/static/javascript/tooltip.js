// BootstrapツールチップのJS
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, {
    container: 'body', // ツールチップを body に配置して位置ズレを防ぐ
    placement: 'top', // 位置を上部に設定
}));

// ページのレイアウト変更時にツールチップの位置を更新
window.addEventListener('resize', () => {
    tooltipList.forEach(tooltip => tooltip.update());
});