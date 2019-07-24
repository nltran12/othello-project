import React from 'react';
import { Row, Col } from 'reactstrap';

const Introduction = (props) =>
    <React.Fragment>
        <Row>
            <Col>
                <h1>[Trivia]</h1>
            </Col>
        </Row>   
        <Row className="top-padding">
            <Col>
                <div className="text-left">
                    <div className="rules-header-text">Game play: </div>
                    <div className="bold">Solo Mode: </div>
                    Challenge yourself and see how many questions you can answer. Game ends if you can no longer answer at least 50% of the questions correctly.<br/>
                    <div className="bold">Versus Mode: </div>
                    Can you beat the computer? Game ends if you and the computer can no longer answer 50% of the questions correctly.
                </div>
            </Col>
        </Row> 
    </React.Fragment>

export default Introduction;