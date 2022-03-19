import {IActions} from "./interfaces";
import { UNICORN_STORE } from '../../constants';
import { Unicorn } from "../../../entities/unicorn";

export const actions: IActions = {
    /**
     * Action that initializes the state when app is loaded
     * @param commit
     */
    [UNICORN_STORE.ACTIONS.INITIALIZE_STORE]({commit}) {
        let unicorn1 = new Unicorn('Pénélope', 'Elle va vite', '../assets/dark_unicorn.jpg', 3.78, 95, 'Coureuse');
        let unicorn2 = new Unicorn('Gertrude', 'Elle fait des calins', '../assets/img/dark_unicorn.jpg', 4.58, 110, 'Volante');
        commit(UNICORN_STORE.MUTATIONS.ADD_UNICORN, unicorn1);
        commit(UNICORN_STORE.MUTATIONS.ADD_UNICORN, unicorn2);
    },

    /**
     * The RETURN_UNICORNS action, will return unicorns from database
     * @param commit
     */
    [UNICORN_STORE.ACTIONS.RETURN_UNICORNS]({commit}) {
        return new Array<Unicorn>();
    }
}
