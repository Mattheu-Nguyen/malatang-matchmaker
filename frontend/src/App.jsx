function App() {
  const handleSubmit = async () => {
    try {
      const response = fetch("http://localhost:5000/recommend", {
        method: "POST", 
        headers: {
          "Content-Type": "application/json",
        },
        body: // preferences
      });
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <>
      <section className="h-screen bg-yellow-200">
        <h1>HELLO</h1>
      </section>
    </>
  );
}

export default App;
