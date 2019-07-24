import {} from '../redux/optionsConstants';
import { UPDATE_PAGE, VALIDATE_URL, UPDATE_DATA } from './actionTypes';

export const setActivePage = (activePage) => ({
    type: UPDATE_PAGE,
    activePage: activePage
});

export const setData = (responseCode, questions) => ({
    type: UPDATE_DATA,
    responseCode: responseCode,
    questions: questions
});

export const updateValidUrl = (isValid) => ({
    type: VALIDATE_URL,
    validUrl: isValid
});