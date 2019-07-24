import React, {Component} from 'react';
import {Row, Col, Button} from 'reactstrap';
import QASet from '../components/QASet';
import ReactHtmlParser from 'react-html-parser'; 
import Score from '../components/Score';

class TriviaGame extends Component {
    constructor(props) {
        super(props);

        this.state = {
            activeQuestion: 0,
            playerScore: 0,
            computerScore: 0,
            nextActive: false,
            answered: false
        };
        this.updateQuestion = this.updateQuestion.bind(this);
        this.updatePlayerScore = this.updatePlayerScore.bind(this);
        this.updateComputerScore = this.updateComputerScore.bind(this);
        this.toggleNextButtonOn = this.toggleNextButtonOn.bind(this);
        this.toggleNextButtonOff = this.toggleNextButtonOff.bind(this);
        this.isGameOver = this.isGameOver.bind(this);
    }

    updateQuestion() {
        this.toggleNextButtonOff();
        if (this.state.activeQuestion < this.props.totalQuestions - 1) {
            this.setState({activeQuestion: this.state.activeQuestion + 1});
        }
    }

    updatePlayerScore() {
        if (this.state.answered === false) {
            this.setState({playerScore: this.state.playerScore + 1});
        }
    }

    updateComputerScore() {
        if (this.state.answered === false) {
            this.setState({computerScore: this.state.computerScore + 1});
        }
    }

    toggleNextButtonOn() {
        if (this.state.answered === false) {
            this.setState({answered: true, nextActive: true});
        }
    }

    toggleNextButtonOff() {
        this.setState({answered: false, nextActive: false});
    }

    isGameOver() {
        let numQuestionsLeft = this.props.totalQuestions - this.state.activeQuestion;
        let halfPoints = Math.floor(this.props.totalQuestions / 2);
        if (this.state.activeQuestion === (this.props.totalQuestions - 1)) {
            return true;
        }
        if (this.props.mode === "computer" && (this.state.computerScore + numQuestionsLeft) > halfPoints) {
            return false;
        }
        if ((this.state.playerScore + numQuestionsLeft) > halfPoints) {
            return false;
        }
        return true;
    }

    render() {
        let nextButton = 
            !this.isGameOver() && this.state.nextActive
            && this.state.activeQuestion !== (this.props.totalQuestions - 1) ?
            <Button outline color="secondary" size="md" onClick={this.updateQuestion}><div className="bold">Next</div></Button> : "";
        
        let playAgainButton = this.isGameOver() && this.state.nextActive ?
            <Button outline color="secondary" size="md" onClick={this.props.updatePage}><div className="bold">Play Again</div></Button> : "";

        return (
            <React.Fragment>
                <Score compScore={this.state.computerScore} 
                    playerScore={this.state.playerScore} 
                    //mode={this.props.mode}
                    gameOver={this.isGameOver()}
                    active={this.state.nextActive}/>
                {
                    this.props.questionSets.map (
                        (questionSet, index) =>
                            index === this.state.activeQuestion ?
                            <QASet
                                key={"set" + index}
                                setNum={index}
                                category={questionSet.category}
                                difficulty={questionSet.difficulty}
                                question={ReactHtmlParser(questionSet.question)}
                                correctAnswer={ReactHtmlParser(questionSet.correct_answer)}
                                incorrectAnswers={questionSet.incorrect_answers}
                                totalQuestions={this.props.totalQuestions}
                                updatePlayerScore={this.updatePlayerScore}
                                updateComputerScore={this.updateComputerScore}
                                mode={this.props.mode}
                                toggleNextButtonOn={this.toggleNextButtonOn}/>
                            : ""
                    )
                }
                <Row>
                    <Col align="right" md={{ size: 10, offset: 1 }} lg={{ size: 8, offset: 2 }}>
                         {nextButton}
                    </Col>
                </Row>
                <Row>
                    <Col align="right" md={{ size: 10, offset: 1 }} lg={{ size: 8, offset: 2 }}>
                         {playAgainButton}
                    </Col>
                </Row>
            </React.Fragment>
        );
    }

}

export default TriviaGame;