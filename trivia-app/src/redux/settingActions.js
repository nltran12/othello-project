import { SET_NUM_QUESTIONS, SET_DIFFICULTY, SET_CATEGORY, SET_PLAY_MODE } from "./actionTypes";

export const setNumQuestions = (numQuestions) => ({
    type: SET_NUM_QUESTIONS,
    numQuestions: numQuestions
});

export const setDifficulty = (difficulty) => ({
    type: SET_DIFFICULTY,
    difficulty: difficulty
});

export const setCategory = (category) => ({
    type: SET_CATEGORY,
    category: category
});

export const setPlayMode = (mode) => ({
    type: SET_PLAY_MODE,
    playMode: mode
});