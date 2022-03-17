import axios, { AxiosRequestConfig, AxiosStatic } from 'axios';
class HttpService {
  protected static instance: HttpService;
  protected static axiosInstance: AxiosStatic;

  protected constructor(axiosInstance: AxiosStatic) {
    HttpService.axiosInstance = axiosInstance;
  }

  public static Instance(): HttpService {
    if (HttpService.instance != undefined) {
      return HttpService.instance;
    }else {
      HttpService.instance = new HttpService(axios);
      return HttpService.instance;
    }
  }

  public get(route: any, params?: AxiosRequestConfig|undefined): Promise<any> {
    return HttpService.axiosInstance.get(route, params)
        .then((response) => {
          return Promise.resolve(response.data);
        }).catch((err) => {
          return Promise.reject(err);
        });
  }

  public post(route: any, body?: any, params?: AxiosRequestConfig|undefined): Promise<any> {
    return HttpService.axiosInstance.post(route, body, params)
        .then((response) => {
          return Promise.resolve(response.data);
        }).catch((err) => {
          return Promise.reject(err);
        });
  }

  public put(route: any, body?: any, params?: AxiosRequestConfig|undefined): Promise<any> {
    return HttpService.axiosInstance.put(route, body, params)
        .then((response) => {
          return Promise.resolve(response.data);
        }).catch((err) => {
          return Promise.reject(err);
        });
  }

  public delete(route: any, params?: AxiosRequestConfig|undefined): Promise<any> {
    return HttpService.axiosInstance.delete(route, params)
        .then((response) => {
          return Promise.resolve(response.data);
        }).catch((err) => {
          return Promise.reject(err);
        });
  }
}

export const Http = HttpService.Instance();