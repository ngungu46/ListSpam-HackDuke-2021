import React from "react";
//import card here

//export this default class
class Body extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            imgs: ["candy.png", "candy.png", "cat.jpeg", "cat.jpeg", "girl.png", "girl.png",
                "pumpkin.jpeg", "pumpkin.jpeg", "snoopy.jpeg", "snoopy.jpeg"]
        }
    }

    //add a function here to shuffle the array when this component is rendered
    //hint: use componentDidMount
    componentDidMount() {
        this.setState({ images: this.shuffleArray(this.state.imgs)}, () => {
            console.log(this.state.imgs);
        });
    }
    //this function is used to shuffle the array
    //You don't need to change this function
    shuffleArray = (array) => {
        for (var i = array.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        return array;
    }

    //complete this function:
    //create an array that contains a Card for each image
    //hint: use a loop
    getImage = () => {
        let imgs = this.state.imgs;
        let newImgs = [];
        imgs.forEach((img, index) => {
            newImgs.push(<Card img={"img/" + img} key={index} />)
        })
        return newImgs;
    }

    render() {
        return (
            <div className="body">
                <div className="row">
                    {this.getImage()}
                </div>
            </div>
        )
    }
}