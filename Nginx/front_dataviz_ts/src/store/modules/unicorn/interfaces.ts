import {MutationTree, ActionContext, ActionTree, GetterTree} from "vuex";
import { UNICORN_STORE } from '../../constants';
import {Unicorn} from "../../../entities/unicorn";

export interface IState {
  unicorns?: Array<Unicorn>
}

export interface IGetters extends GetterTree<IState, IState>  {
  [UNICORN_STORE.GETTERS.GET_UNICORNS](state: IState): Array<Unicorn> | undefined;
}

export interface IMutations extends MutationTree<IState> {
  [UNICORN_STORE.MUTATIONS.ADD_UNICORN](state: IState, unicorn: Unicorn): void;
  [UNICORN_STORE.MUTATIONS.REMOVE_UNICORN](state: IState, id: number): void;
}

export interface IActions extends ActionTree<IState, IState>  {
  [UNICORN_STORE.ACTIONS.INITIALIZE_STORE]({ commit }: ActionContext<IState, IState>): void;
  [UNICORN_STORE.ACTIONS.RETURN_UNICORNS]({ commit }: ActionContext<IState, IState>): Array<Unicorn>;
}