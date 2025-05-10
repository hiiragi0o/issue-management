// BootstrapトーストのJS
document.addEventListener("DOMContentLoaded", function () {
    var toastEls = document.querySelectorAll(".toast");
    toastEls.forEach(function (toastEl) {
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
    });
});


