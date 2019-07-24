import React, {Component} from 'react';
import {Container} from 'reactstrap';
import UserSettings from '../components/UserSettings';
import TriviaGame from '../components/TriviaGame';
import {connect} from 'react-redux';
import {ACTIVE_PAGES} from '../redux/optionsConstants';
import {setActivePage, setData, updateValidUrl} from '../redux/appActions';

const mapStateToProps = (state) => {
    const activePage = state.activePage;
    const responseCode = state.responseCode;
    const questionSets = state.questionSets;
    const validUrl = state.validUrl;
    const numQuestions = state.numQuestions;
    const pickedCategory = state.category;
    const difficulty = state.difficulty;
    const mode = state.playMode;
    return {activePage, responseCode, questionSets, validUrl, numQuestions, pickedCategory, difficulty, mode};
}

class App extends Component {
    constructor(props) {
        super(props);

        this.getData = this.getData.bind(this);
        this.togglePage = this.togglePage.bind(this);
        this.updatePage = this.updatePage.bind(this);
    }

    /**
     * Creates the url string from parameters, gets the data from api, and updates page if data was
     * sucessfully retrieved.
     */
    getData() {
        let currentUrl = "https://opentdb.com/api.php?amount=" + this.props.numQuestions;
        if (this.props.difficulty !== "any difficulty") {
            currentUrl = currentUrl + "&difficulty=" + this.props.difficulty;
        }
        if (this.props.pickedCategory !== -1) {
            currentUrl = currentUrl + "&category=" + this.props.pickedCategory;
        }
        console.log(this.props.mode);
        fetch(currentUrl)
            .then(results => { return results.json(); })
            .then(data => {
                this.props.setData(data.response_code, data.results)
                //this.setState({responseCode: data.response_code, questionSets: data.results})
                this.updatePage();
        })
    }

    updatePage() {
        if (this.props.activePage === ACTIVE_PAGES[0]) {
            if (this.props.responseCode === 0) {
                this.props.setActivePage(ACTIVE_PAGES[1]);
                this.props.updateValidUrl(true);

                //this.setState({activePage: "trivia", validUrl: true});
            } else {
                this.props.updateValidUrl(false);
                //this.setState({validUrl: false});
            }
        } else {
            this.props.setActivePage(ACTIVE_PAGES[0]);
            //this.setState({activePage: "homepage"});
        }
    }

    togglePage() {
        if (this.props.activePage === ACTIVE_PAGES[0]) {
            return <UserSettings 
                    getData={this.getData} 
                    validUrl={this.props.validUrl}/>;
        }
        return <TriviaGame
            updatePage={this.updatePage} 
            mode={this.props.mode}
            totalQuestions={this.props.questionSets.length}
            questionSets={this.props.questionSets}/>;
    }

    render() {
        let currentPage = this.togglePage();

        return (
            <div className="mt-4 mb-4">
                <Container>
                    {currentPage}
                </Container>
            </div>
        )
    }
}

export default connect(mapStateToProps, {setActivePage, setData, updateValidUrl}) (App)
