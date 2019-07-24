import React from 'react';
import { Row, Col } from 'reactstrap';
import Question from '../components/Question';
import Answers from '../components/Answers';


const QASet = (props) =>
    <div>
        <Row className="bottom-padding">
            <Col sm="12" md={{ size: 10, offset: 1 }} lg={{ size: 8, offset: 2 }}>
                <Question category={props.category} 
                    difficulty={props.difficulty} 
                    question={props.question} 
                    questionNum={props.setNum + 1} 
                    totalQuestions={props.totalQuestions}/>
            </Col>
        </Row>
        <Answers correctAnswer={props.correctAnswer} 
            incorrectAnswers={props.incorrectAnswers} 
            id={"set" + props.setNum}
            updatePlayerScore={props.updatePlayerScore}
            updateComputerScore={props.updateComputerScore}
            mode={props.mode}
            toggleNextButtonOn={props.toggleNextButtonOn}/>
    </div>

export default QASet;