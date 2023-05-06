const expression = document.querySelector(".expression");
const result = document.querySelector(".result");
const buttons = document.querySelectorAll(".button");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const buttonText = button.textContent;
    if (buttonText === "C") {
      expression.textContent = "";
      result.textContent = "";
    } else if (buttonText === "=") {
      try {
        const evalResult = eval(expression.textContent);
        result.textContent = evalResult;
      } catch (e) {
        result.textContent = "Error";
      }
    } else {
      expression.textContent += buttonText;
    }
  });
});
