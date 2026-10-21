/*
  ==========================================================================
  script.js : checks the contact form and controls what happens on submit

  This file runs in the browser when contact.html loads. In short, it:
    1. Defines the rules for each field (checkName, checkEmail, checkMessage).
    2. Shows or clears the error message for a field (showFieldResult).
    3. Keeps the message character counter up to date (updateMessageCounter).
    4. Re-checks a field as the user types, once it has an error.
    5. When the form is submitted, checks every field. If all are valid, it
       opens confirmation.html. If not, it shows the errors and keeps the
       user's entries on the page.

  The rules that can be changed easily are the limits and the email pattern
  in the Settings section below.
  ==========================================================================
*/

/* ---- Settings ---- */

// The longest name allowed, in characters.
const NAME_MAX_LENGTH = 100;

// The longest message allowed, in characters.
const MESSAGE_MAX_LENGTH = 2000;

// A pattern that a valid email address must match. In plain terms it means:
//   - one or more characters that are not a space or @
//   - then an @
//   - then one or more characters that are not a space or @
//   - then a full stop (dot)
//   - then one or more characters that are not a space or @
// It catches common mistakes such as a missing @ or a missing dot, but it is
// not a full check of every email address that exists.
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/* ---- Find the elements on the page ----
   document.getElementById looks up an element by its id attribute in
   contact.html. Storing each one in a variable means we only look it up once. */
const form = document.getElementById("contact-form");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const messageInput = document.getElementById("message");
const messageCounter = document.getElementById("message-counter");

/* ---- Validation rules ----
   Each rule function looks at one field and returns:
     - an error message (text) if the field is wrong, or
     - an empty string "" if the field is correct.
   .trim() removes spaces from the start and end of the entry first, so a
   name made only of spaces counts as empty. */

/* Checks the Name field. Returns "" if valid, otherwise an error message. */
function checkName() {
  const value = nameInput.value.trim();

  if (value === "") {
    return "Please enter your name.";
  }
  if (value.length > NAME_MAX_LENGTH) {
    return `Your name is ${value.length} characters. Please use ${NAME_MAX_LENGTH} or fewer.`;
  }
  return "";
}

/* Checks the Email field. Returns "" if valid, otherwise an error message. */
function checkEmail() {
  const value = emailInput.value.trim();

  if (value === "") {
    return "Please enter your email address.";
  }
  // .test() returns true if the value matches EMAIL_PATTERN, false if not.
  if (!EMAIL_PATTERN.test(value)) {
    return "Please enter a valid email address, such as name@example.com.";
  }
  return "";
}

/* Checks the Message field. Returns "" if valid, otherwise an error message. */
function checkMessage() {
  const value = messageInput.value.trim();

  if (value === "") {
    return "Please enter a message.";
  }
  if (value.length > MESSAGE_MAX_LENGTH) {
    return `Your message is ${value.length} characters. Please use ${MESSAGE_MAX_LENGTH} or fewer.`;
  }
  return "";
}

/* ---- List of fields ----
   Each entry in this list pairs one form field with:
     - input: the text box itself
     - error: the paragraph where its error message appears
     - check: the rule function that tests it
   Putting them in one list lets the code loop over all fields the same way. */
const fields = [
  { input: nameInput, error: document.getElementById("name-error"), check: checkName },
  { input: emailInput, error: document.getElementById("email-error"), check: checkEmail },
  { input: messageInput, error: document.getElementById("message-error"), check: checkMessage }
];

/* ---- Showing results ----
   Runs the rule for one field, then updates the page to match:
     - writes the error message (or clears it) under the field
     - adds or removes the "invalid" class, which turns the border red
     - updates aria-invalid, which tells screen readers the field has a problem

   Takes:   field, one entry from the fields list above
   Returns: true if the field is valid, false if not */
function showFieldResult(field) {
  const message = field.check();   // "" when valid, otherwise the error text
  const isValid = message === "";

  field.error.textContent = message;
  // classList.toggle(name, true) adds the class; toggle(name, false) removes it.
  field.input.classList.toggle("invalid", !isValid);
  field.input.setAttribute("aria-invalid", String(!isValid));

  return isValid;
}

/* Updates the message counter, for example "42 / 2000 characters".
   The counter turns red when the message is over the limit. */
function updateMessageCounter() {
  const length = messageInput.value.trim().length;

  messageCounter.textContent = `${length} / ${MESSAGE_MAX_LENGTH} characters`;
  messageCounter.classList.toggle("over-limit", length > MESSAGE_MAX_LENGTH);
}

/* ---- Live feedback while typing ----
   The "input" event fires every time the user types or deletes a character.
   Once a field is showing an error, the check runs again on each keystroke,
   so the error disappears as soon as the problem is fixed. Fields that have
   not yet failed are left alone, so the user is not told about a problem
   before they have finished typing. */
fields.forEach(function (field) {
  field.input.addEventListener("input", function () {
    if (field.input.classList.contains("invalid")) {
      showFieldResult(field);
    }
  });
});

// The counter needs to update on every keystroke in the message box, even
// before any error has appeared.
messageInput.addEventListener("input", updateMessageCounter);

// Set the counter to "0 / 2000 characters" when the page first loads.
updateMessageCounter();

/* ---- Submitting the form ----
   The "submit" event fires when the user clicks "Send message" or presses
   Enter in a text box. */
form.addEventListener("submit", function (event) {
  // By default the browser would send the form and reload the page, losing
  // what the user typed. preventDefault() stops that, so the entries stay put.
  event.preventDefault();

  let allValid = true;           // Becomes false if any field fails
  let firstInvalidInput = null;  // Remembers the first field with a problem

  // Check every field, not just the first one, so all the errors show at once.
  fields.forEach(function (field) {
    const isValid = showFieldResult(field);

    if (!isValid) {
      allValid = false;
      // Only record the first problem field. The "=== null" test is true
      // only until the first one has been stored.
      if (firstInvalidInput === null) {
        firstInvalidInput = field.input;
      }
    }
  });

  // If anything is wrong, move the cursor to the first problem field and stop.
  if (!allValid) {
    firstInvalidInput.focus();
    return;
  }

  // Every field is valid, so move the user to the thank-you page.
  // Setting window.location.href loads a new page in the same browser tab.
  window.location.href = "confirmation.html";
});
