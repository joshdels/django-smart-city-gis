const email = document.getElementById("email");
const password = document.getElementById("initialPassword");
const confirmPassword = document.getElementById("confirmPassword");
const registerBtn = document.getElementById("registerBtn");
const passwordError = document.getElementById("passwordError");
const emailError = document.getElementById("emailError");

function validateForm() {
  const emailValid = email.checkValidity();

  if (!emailValid) {
    emailError.textContent = "Enter a valid email";
  } else {
    emailError.textContent = "";
  }

  const passwordsMatch =
    password.value !== "" && password.value === confirmPassword.value;

  if (email.value !== "" && !emailValid) {
      emailError.textContent = "Enter a valid email";
  } else {
      emailError.textContent = "";
  }

  registerBtn.disabled = !(emailValid && passwordsMatch);
}

email.addEventListener("blur", validateForm);
password.addEventListener("input", validateForm);
confirmPassword.addEventListener("input", validateForm);

validateForm();

