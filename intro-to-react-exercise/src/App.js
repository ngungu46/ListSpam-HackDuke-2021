import './App.css';
import React from "react";
// import body class here


export default class App extends React.Component {

  render() {
    return (
      <div className="app">
        <div className="top">
          <h1>Card Flip Game</h1>
        </div>
        {/* add the body here */}
        <Body />
      </div>
    );
  }
}


