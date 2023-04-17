import logo from './logo.svg';
import React from 'react';
import LaserEffect from './components/LaserEffect';
import SoundCloudPlayer from './components/SoundCloudPlayer';
import './App.css';

function App() {
    const soundcloudEmbedURL =
      'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1237568050';
  
  return (
    <div className="App">
      <LaserEffect />
      <SoundCloudPlayer url={soundcloudEmbedURL} />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
