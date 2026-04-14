
function validateForm() {
    let title = document.getElementById("title").value;
    let genre = document.getElementById("genre").value;
    let description = document.getElementById("description").value;
    let image = document.getElementById("image").value;

    if (!title || !genre || !description || !image) {
        alert("All fields are required!");
        return false;
    }

    let allowed = ["jpg", "jpeg", "png", "gif"];
    let fileExt = image.split('.').pop().toLowerCase();

    if (!allowed.includes(fileExt)) {
        alert("Only image files allowed!");
        return false;
    }

    return true;
}