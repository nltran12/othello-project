import React, { Component } from 'react';
import { Button, Row, Col } from 'reactstrap';
import ReactHtmlParser from 'react-html-parser'; 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheckCircle, faTimesCircle, faDesktop } from '@fortawesome/free-solid-svg-icons';


class Answers extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            active: false,
            activeBtn: null,
            answers: [],
            computerAnswer: Math.floor(Math.random() * (this.props.incorrectAnswers.length + 1)),
            correctAnswerIndex: Math.floor(Math.random() * (this.props.incorrectAnswers.length + 1))
        };

        this.handleClick = this.handleClick.bind(this);
        this.populateAnswerList = this.populateAnswerList.bind(this);
        this.disableBtn = this.disableBtn.bind(this);
    }

    componentWillMount() {
        this.populateAnswerList();
    }

    populateAnswerList() {
        const tempAnswers = this.props.incorrectAnswers;
        tempAnswers.splice(this.state.correctAnswerIndex, 0, this.props.correctAnswer);
        this.setState({ answers: tempAnswers });
    }

    handleClick(index) {
        this.setState({ active:  true, activeBtn: index});
        if (this.state.correctAnswerIndex === index) {
            this.props.updatePlayerScore();
        }
        if (this.state.correctAnswerIndex === this.state.computerAnswer) {
            this.props.updateComputerScore();
        }
        this.props.toggleNextButtonOn();
    }

    disableBtn(index) {
        if (this.state.active === true && this.state.activeBtn !== index) {
            return true;
        }
        return false;
    }

    render() {
        return (
            <div className="answer-padding">
                {
                    this.state.answers.map ((answer, index) => 
                        <Row lg="12" className="bottom-padding" key={this.props.id + "q" + index}>
                            <Col md={{ size: 10, offset: 1 }} lg={{ size: 8, offset: 2 }}>
                                <Button outline color="info" size="lg" block
                                        onClick={() => this.handleClick(index)}
                                        active={this.state.activeBtn === index}
                                        disabled={this.disableBtn(index)}>
                                        <div className="answer-text bold">
                                            {this.props.mode === "computer" && this.state.computerAnswer === index ? 
                                                <FontAwesomeIcon className="fa-fw fa-lg right-spacing" icon={faDesktop}/> : ""}
                                            {ReactHtmlParser(answer)}
                                            {this.state.active === true && this.state.correctAnswerIndex === index ? 
                                                <FontAwesomeIcon className="fa-fw fa-lg" icon={faCheckCircle}/> : ""}
                                            {this.state.activeBtn === index && this.state.correctAnswerIndex !== index ? 
                                                <FontAwesomeIcon className="fa-fw fa-lg" icon={faTimesCircle}/> : ""}
                                        </div>
                                </Button>
                            </Col>
                        </Row>)
                }    
            </div> 
        );
    }
}

export default Answers;