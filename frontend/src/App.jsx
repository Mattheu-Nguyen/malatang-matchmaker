import { useState, useRef, useEffect } from "react";
import confetti from "canvas-confetti";
import logo from "./assets/Header 1.png";
import divider from "./assets/Footer 1.png";
import imgMild from "./assets/IMG_8134.PNG";
import imgMedium from "./assets/IMG_8135.PNG";
import imgSpicy from "./assets/IMG_8136.PNG";
import imgExtraSpicy from "./assets/IMG_8137.PNG";

// steps
import step1 from "./assets/step 1_ choose your spice level.png";
import step2 from "./assets/step 2_ choose your soup base.png";
import step3 from "./assets/step 3_ choose your meat.png";
import step4 from "./assets/step 4_ choose your ingredients.png";
import step5 from "./assets/step 5_ choose your side dishes.png";

// Broth
import imgMala from "./assets/IMG_8141.PNG";
import imgTomato from "./assets/IMG_8142.PNG";
import imgBoneBroth from "./assets/IMG_8144.PNG";
import imgTomYum from "./assets/IMG_8145.PNG";
import imgMushroomBroth from "./assets/IMG_8146.PNG";

// Meats
import imgBeef from "./assets/IMG_8147.PNG";
import imgPork from "./assets/IMG_8149.PNG";
import imgChicken from "./assets/IMG_8150.PNG";
import imgLamb from "./assets/IMG_8151.PNG";
import imgSeafood from "./assets/IMG_8152.PNG";

// Ingredients
import imgFishBall from "./assets/IMG_8159.PNG";
import imgFishCake from "./assets/IMG_8160.PNG";
import imgMushroom from "./assets/IMG_8161.PNG";
import imgNoodles from "./assets/IMG_8162.PNG";
import imgEggs from "./assets/IMG_8163.PNG";
import imgTofu from "./assets/IMG_8164.PNG";
import imgVeggies from "./assets/IMG_8166.PNG";

// Side dishes
import imgSausage from "./assets/sausage.png";
import imgSquid from "./assets/squiddie.png";

const SPICE_LEVELS = [
  { label: "mild", src: imgMild },
  { label: "medium", src: imgMedium },
  { label: "spicy", src: imgSpicy },
  { label: "extra spicy", src: imgExtraSpicy },
];

const BROTH_OPTIONS = [
  { label: "mala", src: imgMala },
  { label: "tomato", src: imgTomato },
  { label: "bone broth", src: imgBoneBroth },
  { label: "tom yum", src: imgTomYum },
  { label: "mushroom", src: imgMushroomBroth },
];

const MEAT_OPTIONS = [
  { label: "beef", src: imgBeef },
  { label: "pork", src: imgPork },
  { label: "chicken", src: imgChicken },
  { label: "lamb", src: imgLamb },
  { label: "seafood", src: imgSeafood },
];

const INGREDIENT_OPTIONS = [
  { label: "fish ball", src: imgFishBall },
  { label: "fish cake", src: imgFishCake },
  { label: "tofu", src: imgTofu },
  { label: "mushroom", src: imgMushroom },
  { label: "noodles", src: imgNoodles },
  { label: "eggs", src: imgEggs },
  { label: "veggies", src: imgVeggies },
];

const SIDE_OPTIONS = [
  { label: "rice" },
  { label: "fried dough" },
  { label: "sesame noodles" },
];

/** Shape matches `/recommend` JSON. Toggle with `VITE_MOCK_RECOMMEND=true` in `.env.local`. */
const MOCK_RECOMMEND_RESPONSE = {
  message: "ok",
  recommended_place: {
    name: "Mock Malatang Palace",
    tagline: "Edit MOCK_RECOMMEND_RESPONSE in App.jsx to try different copy.",
    match_detail: "No backend required — this is static mock data.",
  },
};

function toggleListItem(setter, item) {
  setter((prev) =>
    prev.includes(item) ? prev.filter((x) => x !== item) : [...prev, item],
  );
}

function fireCelebrationConfetti() {
  if (
    typeof window !== "undefined" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches
  ) {
    return;
  }
  const defaults = { origin: { y: 0.62 }, zIndex: 9999 };
  confetti({ ...defaults, particleCount: 100, spread: 65, startVelocity: 40 });
  window.setTimeout(() => {
    confetti({
      ...defaults,
      particleCount: 70,
      spread: 100,
      startVelocity: 28,
      scalar: 0.9,
    });
  }, 180);
}

function PreferenceTile({ label, src, selected, onToggle }) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className={`flex min-h-[11rem] min-w-[8.5rem] flex-col items-center justify-center gap-2 rounded-xl border-2 p-4 text-base font-medium transition-colors sm:min-h-[12rem] sm:min-w-[10rem] ${
        selected
          ? "border-red-600 bg-red-500/30 text-white ring-2 ring-red-600 ring-offset-2"
          : "border-gray-300 bg-gray-50 hover:bg-gray-100"
      }`}
    >
      {src ? (
        <img
          src={src}
          alt={label}
          className="h-24 w-24 shrink-0 object-contain sm:h-28 sm:w-28"
        />
      ) : null}
      <span className="px-1">{label}</span>
    </button>
  );
}

function App() {
  const [spice, setSpice] = useState([]);
  const [broth, setBroth] = useState([]);
  const [meat, setMeat] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const [side, setSide] = useState([]);
  const [recommendedPlace, setRecommendedPlace] = useState(null);
  const [submitError, setSubmitError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const resultsRef = useRef(null);

  useEffect(() => {
    if (!recommendedPlace) return;

    const reducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;

    const t = window.setTimeout(() => {
      resultsRef.current?.scrollIntoView({
        behavior: reducedMotion ? "auto" : "smooth",
        block: "start",
      });
      fireCelebrationConfetti();
    }, 0);

    return () => window.clearTimeout(t);
  }, [recommendedPlace]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const preferences = {
      spice,
      broth,
      meat,
      ingredients,
      side,
    };

    setSubmitError(null);
    setRecommendedPlace(null);
    setIsLoading(true);

    try {
      if (import.meta.env.VITE_MOCK_RECOMMEND === "true") {
        await new Promise((r) => setTimeout(r, 450));
        setRecommendedPlace(MOCK_RECOMMEND_RESPONSE.recommended_place);
        return;
      }

      const response = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(preferences),
      });

      const data = await response.json();
      console.log("Response from server:", data);

      if (!response.ok) {
        throw new Error(data.message || "Request failed");
      }

      if (data.recommended_place) {
        setRecommendedPlace(data.recommended_place);
      } else {
        setSubmitError("No recommendation returned. Try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      setSubmitError(
        error instanceof Error ? error.message : "Something went wrong.",
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <section>
        <img src={logo} className="mx-auto"></img>
        <img src={divider} className="mx-auto"></img>
        <div className="relative mx-auto w-full max-w-5xl px-4">
          <form
            onSubmit={handleSubmit}
            className="mx-auto flex w-full max-w-5xl flex-col space-y-6 p-6 text-center md:p-8"
          >
            <img
              src={step1}
              alt="Step 1: choose your spice level"
              className="mx-auto h-auto w-full max-w-md object-contain"
            />
            <div className="flex flex-wrap justify-center gap-4 sm:gap-5">
              {SPICE_LEVELS.map(({ label, src }) => (
                <PreferenceTile
                  key={label}
                  label={label}
                  src={src}
                  selected={spice.includes(label)}
                  onToggle={() => toggleListItem(setSpice, label)}
                />
              ))}
            </div>

            <img
              src={step2}
              alt="Step 2: choose your soup base"
              className="mx-auto h-auto w-full max-w-md object-contain"
            />
            <div className="flex flex-wrap justify-center gap-4 sm:gap-5">
              {BROTH_OPTIONS.map(({ label, src }) => (
                <PreferenceTile
                  key={label}
                  label={label}
                  src={src}
                  selected={broth.includes(label)}
                  onToggle={() => toggleListItem(setBroth, label)}
                />
              ))}
            </div>

            <img
              src={step3}
              alt="Step 3: choose your meat"
              className="mx-auto h-auto w-full max-w-md object-contain"
            />
            <div className="flex flex-wrap justify-center gap-4 sm:gap-5">
              {MEAT_OPTIONS.map(({ label, src }) => (
                <PreferenceTile
                  key={label}
                  label={label}
                  src={src}
                  selected={meat.includes(label)}
                  onToggle={() => toggleListItem(setMeat, label)}
                />
              ))}
            </div>

            <img
              src={step4}
              alt="Step 4: choose your ingredients"
              className="mx-auto h-auto w-full max-w-md object-contain"
            ></img>
            <div className="flex flex-wrap justify-center gap-4 sm:gap-5">
              {INGREDIENT_OPTIONS.map(({ label, src }) => (
                <PreferenceTile
                  key={label}
                  label={label}
                  src={src}
                  selected={ingredients.includes(label)}
                  onToggle={() => toggleListItem(setIngredients, label)}
                />
              ))}
            </div>

            <img src={step5} alt="Step 5: choose your side dishes" className="mx-auto h-auto w-full max-w-md object-contain"
            ></img>
            <div className="flex flex-wrap justify-center gap-4 sm:gap-5">
              {SIDE_OPTIONS.map(({ label, src }) => (
                <PreferenceTile
                  key={label}
                  label={label}
                  src={src}
                  selected={side.includes(label)}
                  onToggle={() => toggleListItem(setSide, label)}
                />
              ))}
            </div>

            {submitError ? (
              <p className="text-center text-sm text-red-700" role="alert">
                {submitError}
              </p>
            ) : null}

            {isLoading ? (
              <div className="flex justify-center">
                <div className="h-8 w-8 animate-spin rounded-full border-b-2 border-t-2 border-green-500"></div>
              </div>
            ) : (
              <button
                type="submit"
                className="rounded bg-green-500 px-4 py-2 text-white hover:bg-green-600"
              >
                Submit
              </button>
            )}
          </form>
        </div>
      </section>

      <section
        id="results"
        ref={resultsRef}
        aria-live="polite"
        className="scroll-mt-4 flex min-h-screen flex-col items-center justify-center border-t border-amber-200/80 bg-[#F9F1D2] px-4 py-8"
      >
        <div className="mx-auto w-full max-w-lg text-center">
          {recommendedPlace ? (
            <div className="rounded-2xl border-2 border-red-600/40 bg-white/90 p-8 shadow-lg ring-2 ring-amber-100">
              <p className="text-sm font-semibold uppercase tracking-wide text-red-700">
                Your match
              </p>
              <h2 className="mt-2 font-serif text-3xl font-bold text-gray-900 sm:text-4xl">
                {recommendedPlace.name}
              </h2>
              {recommendedPlace.tagline ? (
                <p className="mt-3 text-lg text-gray-700">
                  {recommendedPlace.tagline}
                </p>
              ) : null}
              {recommendedPlace.match_detail ? (
                <p className="mt-2 text-base text-gray-600">
                  {recommendedPlace.match_detail}
                </p>
              ) : null}
            </div>
          ) : (
            <p className="text-gray-500">
              Submit your preferences above to see your recommended spot.
            </p>
          )}
        </div>
      </section>
    </>
  );
}

export default App;
