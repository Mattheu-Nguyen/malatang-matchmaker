// =============================================================================
// js/main.js — Person 4 (Frontend Developer)
// =============================================================================
// PURPOSE:
//   Handle form submission on index.html:
//     1. Collect user preferences from the form
//     2. Send a POST request to the Flask backend
//     3. Display results (or redirect to results.html with data)
//
// Also handles displaying results on results.html.
// =============================================================================


// -----------------------------------------------------------------------------
// CONFIGURATION
// -----------------------------------------------------------------------------
// TODO: Set the backend API URL as a constant at the top so it's easy to change
//   const API_URL = 'http://localhost:5000/recommend';


// =============================================================================
// INDEX.HTML LOGIC — Form submission
// =============================================================================

// -----------------------------------------------------------------------------
// STEP 1: Wait for the page to load
// -----------------------------------------------------------------------------
// TODO: Add a DOMContentLoaded event listener so your code runs after the HTML loads
//   document.addEventListener('DOMContentLoaded', function() { ... });


// -----------------------------------------------------------------------------
// STEP 2: Grab references to DOM elements
// -----------------------------------------------------------------------------
// TODO: Get the form element by ID:        document.getElementById('preference-form')
// TODO: Get the loading div by ID:         document.getElementById('loading')
// TODO: Get the error message div by ID:   document.getElementById('error-msg')


// -----------------------------------------------------------------------------
// STEP 3: Listen for form submit
// -----------------------------------------------------------------------------
// TODO: Add a 'submit' event listener to the form
// TODO: Call event.preventDefault() to stop the page from refreshing


// -----------------------------------------------------------------------------
// STEP 4: Collect form values into an object
// -----------------------------------------------------------------------------
// Read each input field and build the preferences object.
// The keys here MUST match what Person 3 expects in the recommendation engine!
//
// Example for a dropdown:
//   const spiceLevel = document.getElementById('spice-level').value;
//
// Example for checkboxes (collecting all checked values into an array):
//   const meats = Array.from(document.querySelectorAll('input[name="meats"]:checked'))
//                      .map(cb => cb.value);
//
// TODO: Collect spice_level   (dropdown value)
// TODO: Collect broth         (dropdown value)
// TODO: Collect meats         (array of checked checkbox values)
// TODO: Collect ingredients   (array of checked checkbox values)
// TODO: Collect side_dishes   (array of checked checkbox values)
//
// TODO: Build the preferences object:
//   const preferences = {
//     spice_level: spiceLevel,
//     broth: broth,
//     meats: meats,
//     ingredients: ingredients,
//     side_dishes: sideDishes
//   };


// -----------------------------------------------------------------------------
// STEP 5: Show loading state
// -----------------------------------------------------------------------------
// TODO: Remove the 'hidden' class from the loading element
// TODO: Add the 'hidden' class to the error message element (clear any old error)


// -----------------------------------------------------------------------------
// STEP 6: Send the POST request to the backend
// -----------------------------------------------------------------------------
// Use the fetch() API to POST the preferences as JSON.
//
// TODO: Call fetch(API_URL, { ... })
//   Options needed:
//     method: 'POST'
//     headers: { 'Content-Type': 'application/json' }
//     body: JSON.stringify(preferences)
//
// TODO: Chain .then(response => response.json())  to parse the JSON response
// TODO: Chain .then(data => { ... })              to handle the results
// TODO: Chain .catch(error => { ... })            to handle network errors


// -----------------------------------------------------------------------------
// STEP 7: Handle the response — display results or redirect
// -----------------------------------------------------------------------------
// OPTION A (simpler): Display results directly on index.html below the form
//   - Create restaurant cards and append them to a results container div
//
// OPTION B (nicer UX): Save results to sessionStorage and redirect to results.html
//   - sessionStorage.setItem('results', JSON.stringify(data));
//   - window.location.href = 'results.html';
//
// TODO: Choose one approach and implement it
// TODO: Handle empty results (show a "no matches" message)
// TODO: Hide the loading indicator when done


// =============================================================================
// RESULTS.HTML LOGIC — Display results
// =============================================================================
// (Only needed if you chose OPTION B above — redirecting to results.html)

// -----------------------------------------------------------------------------
// STEP 8: On results.html, read data from sessionStorage and render cards
// -----------------------------------------------------------------------------
// TODO: Check if we're on results.html (e.g., check for #results-container)
// TODO: Read: const results = JSON.parse(sessionStorage.getItem('results'));
// TODO: If results is empty or null, show the #no-results message
// TODO: Otherwise, loop through results and create a card for each restaurant


// -----------------------------------------------------------------------------
// STEP 9: Build a restaurant card element
// -----------------------------------------------------------------------------
// This helper function creates a DOM element for one restaurant.
//
// TODO: Define function createRestaurantCard(restaurant) { ... }
// TODO: Create a <div class="restaurant-card">
// TODO: Add <h3> with restaurant.name
// TODO: Add <p> with restaurant.address + ', ' + restaurant.city
// TODO: Add <p> with star rating — convert restaurant.stars to ⭐ characters
//       e.g., "⭐ 4.5" or filled/empty star icons
// TODO: Add <p> with match score — e.g., "Match: 87%"
// TODO: Return the card element


// =============================================================================
// TESTING TIP:
// Before the backend is ready, you can test the UI with fake data.
// Comment out the fetch() call and use this instead:
//
// const fakeResults = [
//   { name: "Mala Hot Pot", address: "123 Main St", city: "San Francisco", stars: 4.5, match_score: 87 },
//   { name: "Spicy Bowl", address: "456 Elm Ave", city: "Oakland", stars: 4.2, match_score: 74 }
// ];
// handleResults(fakeResults);
// =============================================================================
