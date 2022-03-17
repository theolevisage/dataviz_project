import {IState} from "./interfaces";
import {IGetters} from "./interfaces";
import { UNICORN_STORE } from '../../constants';
import {Unicorn} from "../../../entities/unicorn";


export const getters: IGetters = {
    [UNICORN_STORE.GETTERS.GET_UNICORNS](state: IState): Array<Unicorn> | undefined {
        return state.unicorns;
    }
}