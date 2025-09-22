import { useEffect, useState } from "react";
import "./App.css";

function Input({ type, classs, placeholder, onchange }) {
  return (
    <input
      type={type}
      className={classs}
      placeholder={placeholder}
      onChange={(e) => onchange(e.target.value)}
    />
  );
}

function Button({ classs, children, onClick }) {
  return <button className={classs} children={children} onClick={onClick} />;
}

function Form({ classs }) {
  const [url, setUrl] = useState("");

  const download = async (targeturl) => {
    if (!targeturl) return console.warn("Veuillez entrer une URL valide");
    try {
      const response = await fetch(`http://127.0.0.1:8000/download/video?url=${encodeURIComponent(targeturl)}`);
      if (!response.ok) throw new Error("Erreur de connexion au serveur");
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div className={classs}>
      <Input
        type={"text"}
        classs={"input-url"}
        placeholder={"Coller l'url de la video/playlist"}
        onchange={ setUrl }
        vvalue={url}
      />
      <Button 
        classs={"btn-submit"}
        children={"Download"}
        onClick={ () => download(url) }
      />
    </div>
  );
}

function App() {
  return (
    <>
      <h1 className="title">Yt-Dowloader</h1>
      <Form classs="form-url" />
    </>
  );
}

export default App;
