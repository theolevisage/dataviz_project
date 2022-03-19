import {IState} from "./interfaces";
import {IMutations} from "./interfaces";
import { UNICORN_STORE } from '../../constants';
import { Unicorn } from "../../../entities/unicorn";

export const mutations: IMutations = {
    [UNICORN_STORE.MUTATIONS.ADD_UNICORN](state: IState, unicorn: Unicorn) {
        if (state.unicorns) {
            state.unicorns.push(unicorn);
        }else{
            state.unicorns = new Array<Unicorn>();
            state.unicorns.push(unicorn);
        }
    },
    [UNICORN_STORE.MUTATIONS.REMOVE_UNICORN](state: IState, id: number) {
        // TODO
        console.log(state)
        console.log(id)
        return;
    },
}