async function uploadImage() {
  const fileInput = document.getElementById("imageUpload");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please choose an image first!");
    return;
  }

  // Preview the image
  const preview = document.getElementById("preview");
  preview.innerHTML = `<img src="${URL.createObjectURL(file)}" />`;

  // Send image to backend
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  // Show result
  document.getElementById("result").innerHTML = `
    <h3>Prediction: ${data.label}</h3>
    <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
  `;
}
