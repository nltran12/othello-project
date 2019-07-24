import React from 'react';
import { Row, Col } from 'reactstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faDesktop, faUserAlt } from '@fortawesome/free-solid-svg-icons';
import { PLAY_MODE } from '../redux/optionsConstants';

/**
 * Returns the computer score display if it's versus computer mode.
 */
function getComputerScore(mode, score) {
    if (mode === PLAY_MODE[1]) {
        return  ":" + score;
    }
    return "";
}

const Score = (props) =>
    <div>
        <Row><Col align="center">{props.gameOver && props.active ? <p className="game-over-text bold">Game Over!</p> : ""}</Col></Row>
        <Row>
            <Col lg={{size: 8, offset: 2}} align="right">
                <h2>
                    <FontAwesomeIcon className="fa-md" icon={faUserAlt}/>:{props.playerScore}
                    {props.mode === "computer" ? <FontAwesomeIcon className="fa-md left-spacing" icon={faDesktop}/>:""}
                    {getComputerScore(props.mode, props.compScore)}
                </h2>
            </Col>
        </Row>
    </div>

export default Score;