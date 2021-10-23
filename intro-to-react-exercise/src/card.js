import React from "react"

//export this default class
class Card extends React.Component {

    //this function rotates the card when it is clicked on
    //You don't need to modify this function
    onClick = (event) => {
        let element = event.currentTarget;
        if (element.className === "card-inner") {
        if(element.style.transform === "rotateY(180deg)") {
          element.style.transform = "rotateY(0deg)";
        }
        else {
          element.style.transform = "rotateY(180deg)";
        }
      }
    };

    render() {
        return (
            <div className="column">
                <div className="card">
                    <div className="card-inner" onClick={this.onClick}>
                        <div className="front">
                            <p>Card</p>
                        </div>
                        <div className="back">
                            {/* create an img that uses props to get img src */}
                            <img src={this.props.img} alt={this.props.img} />
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}