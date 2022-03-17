import { createStore } from 'vuex';
import auth from './modules/unicorn/index'

export default createStore({
    modules: { auth }
});