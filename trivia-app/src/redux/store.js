import { createStore } from "redux";
import {INITIAL_STATE} from "../redux/optionsConstants";
import { SET_NUM_QUESTIONS, SET_DIFFICULTY, SET_CATEGORY, UPDATE_DATA, VALIDATE_URL, UPDATE_PAGE } from "../redux/actionTypes";

function rootReducer(state = INITIAL_STATE, action) {
    switch(action.type) {
        case SET_NUM_QUESTIONS:
            return {...state, numQuestions: action.numQuestions}
        case SET_DIFFICULTY:
            return {...state, difficulty: action.difficulty}
        case SET_CATEGORY:
            return {...state, category: action.category}
        case UPDATE_PAGE:
            return {...state, activePage: action.activePage}
        case UPDATE_DATA:
            return {...state, responseCode: action.responseCode, questionSets: action.questions}
        case VALIDATE_URL:
            return {...state, validUrl: action.validUrl}
        default:
            return state;
    }
    
}

export default createStore(rootReducer);