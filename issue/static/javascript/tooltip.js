// BootstrapツールチップのJS
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');

const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, {
    container: 'body', // ツールチップを body に配置して位置ズレを防ぐ
    placement: 'auto', // 自動的に位置を調整
    boundary: 'window', // ツールチップの境界をウィンドウに設定
}));
