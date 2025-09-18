
import { useState } from 'react'
import './App.css'

function Input({ type, classs, placeholder, onchange }){
  return <input 
    type={type} 
    className={classs} 
    placeholder={placeholder}
    onChange={ (e) => onchange(e.target.value) }
  />
}

function Button({classs,children}){
  return <button className={classs}>{children}</button>
}

function Form({classs}){
  const [url, setUrl] = useState('')

  return <div className={classs}>
    <Input
      type='text'
      classs="input-url"
      placeholder="Coller l'url de la video/playlist"
      onchange={ setUrl }
    />
    <Button classs="btn-submit">Dowload</Button>
  </div>
}

function App() {
  return <>
    <h1 className='title'>Yt-Dowloader</h1>
    <Form classs='form-url'/>
  </>
}

export default App
