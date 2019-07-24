import React from 'react';
import { Row, Col } from 'reactstrap';

const Question = (props) =>
    <div className="question-border top-padding bottom-padding">
        <Row><Col><p>question {props.questionNum} out of {props.totalQuestions}</p></Col></Row>
        <Row>
            <Col md="7"><p>category: {props.category}</p></Col>
            <Col><p>difficulty: {props.difficulty}</p></Col>
        </Row>   
        <Row>
            <Col><p className="question-text bold">{props.question}</p></Col>
        </Row>  
    </div>

export default Question;