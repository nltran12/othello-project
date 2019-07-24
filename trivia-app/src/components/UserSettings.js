import React, {Component} from 'react';
import {Row, Col, Button, FormGroup, Input, Label, FormFeedback} from 'reactstrap';
import Introduction from './Introduction';
import {connect} from 'react-redux';
import {DIFFICULTIES, CATEGORIES, PLAY_MODE} from '../redux/optionsConstants';
import {setNumQuestions, setCategory, setDifficulty, setPlayMode} from '../redux/settingActions';

const mapStateToProps = (state) => {
    const numQuestions = state.numQuestions;
    const pickedCategory = state.category;
    const difficulty = state.difficulty;
    const playMode = state.playMode;
    return { numQuestions, pickedCategory, difficulty, playMode };
};

function isQuestionsValid(input) {
    if (input === "" || isNaN(input)) {
        return false;
    }
    if (JSON.stringify(input).includes(".") || input > 50 || input < 10) {
        return false;
    }
    return true;
}

class UserSettings extends Component {
    constructor(props) {
        super(props);

        this.updateNumQuestions = this.updateNumQuestions.bind(this);
        this.updateDifficulty = this.updateDifficulty.bind(this);
        this.updateCategory = this.updateCategory.bind(this);
        this.updateMode = this.updateMode.bind(this);
    }

    updateNumQuestions(event) {
        this.props.setNumQuestions(event.target.value);
    }

    updateDifficulty(event) {
        this.props.setDifficulty(event.target.value);
    }

    updateCategory(event) {
        this.props.setCategory(event.target.value);
    }

    updateMode(event) {
        this.props.setPlayMode(event.target.id);
    }

    render() {
        return (
            <React.Fragment>
                    <Introduction/>
                    <Row className="top-padding">
                        <Col md="4" lg="3">
                            <FormGroup>
                                <Label className="bold" for="numQuestions">Number of Questions</Label>
                                <Input 
                                    type="text" 
                                    name="numQuestions" 
                                    id="numQuestions" 
                                    value={this.props.numQuestions} 
                                    valid={isQuestionsValid(this.props.numQuestions)} 
                                    invalid={!isQuestionsValid(this.props.numQuestions)} 
                                    onChange={this.updateNumQuestions}/>
                                <FormFeedback>Must be a whole number between 10 and 50</FormFeedback>
                            </FormGroup>
                        </Col>
                        <Col md="3" lg="2">
                            <FormGroup>
                                <Label className="bold" for="difficulty">Difficulty</Label>
                                <Input 
                                    type="select" 
                                    name="difficulty" 
                                    id="difficultySelect" 
                                    aria-label="difficulty select"
                                    value={this.props.difficulty} 
                                    onChange={this.updateDifficulty}>
                                    {
                                        DIFFICULTIES.map((difficulty, index) =>
                                            <option key={index} value={difficulty}>
                                                {difficulty}
                                            </option>
                                        )
                                    }
                                </Input>
                            </FormGroup>
                        </Col>
                        <Col md="5">
                            <FormGroup>
                                <Label className="bold" for="category">Category</Label>
                                <Input 
                                    type="select" 
                                    name="category" 
                                    id="categorySelect" 
                                    aria-label="category select"
                                    value={this.props.pickedCategory}
                                    onChange={this.updateCategory}>
                                        {
                                            CATEGORIES.map ((category) =>
                                                <option value={category.id} key={category.name} value={category.id}>{category.name}</option>
                                            )
                                        }
                                </Input>
                            </FormGroup>
                        </Col>
                        <Col >
                            <FormGroup check>
                                <Label className="bold">Game Mode:</Label>
                                {PLAY_MODE.map((mode, index) =>
                                    <FormGroup check>
                                        <Label check>
                                            <Input 
                                                type="radio" 
                                                name="GameMode" 
                                                id={index}
                                                checked={this.props.playMode === index}
                                                onChange={this.updateMode}/>{' '}
                                                {mode}
                                        </Label>
                                    </FormGroup>
                                    )
                                }
                            </FormGroup>
                        </Col>
                    </Row>
                    <Row className="top-padding">
                        <Col>
                            <Button 
                                outline color="secondary" 
                                size="lg" 
                                onClick={this.props.getData} 
                                disabled={!isQuestionsValid(this.props.numQuestions)}>
                                    <div className="bold">Start!</div>
                            </Button>
                        </Col>
                    </Row>
                    <Row> 
                        <Col>
                            {!this.props.validUrl ? 
                                <p className="top-padding warning-text bold">Not enough questions available for the following trivia settings.
                                    Please change your settings.</p>:""}
                        </Col>
                    </Row>
                </React.Fragment>
        );
    }
    
}
export default connect(mapStateToProps, {setNumQuestions, setCategory, setDifficulty, setPlayMode})(UserSettings);