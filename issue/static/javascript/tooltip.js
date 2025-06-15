// BootstrapツールチップのJS
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, {
    container: 'body', // ツールチップを body に配置して位置ズレを防ぐ
}));