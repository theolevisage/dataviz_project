import { useToast, TYPE, ToastInterface } from "vue-toastification";
import { ToastContent, ToastOptions } from "vue-toastification/dist/types/types";
class NotificationService {
    protected static instance: NotificationService;
    protected static vueToastificationInstance : ToastInterface;

    protected constructor( vueToastificationInstance : ToastInterface ) {
        NotificationService.vueToastificationInstance = vueToastificationInstance;
    }

    public static Instance(): NotificationService {
        if (NotificationService.instance != undefined) {
            return NotificationService.instance;
        }else {
            const toast = useToast();
            NotificationService.instance = new NotificationService(toast);
            return NotificationService.instance;
        }
    }

    public [TYPE.SUCCESS](content: ToastContent, options?: (ToastOptions & {type?: TYPE.SUCCESS | undefined}) | undefined) {
        return NotificationService.vueToastificationInstance.success(content, options);
    }
    public [TYPE.INFO](content: ToastContent, options?: (ToastOptions & {type?: TYPE.INFO | undefined}) | undefined) {
        return NotificationService.vueToastificationInstance.info(content, options);
    }
    public [TYPE.ERROR](content: ToastContent, options?: (ToastOptions & {type?: TYPE.ERROR | undefined}) | undefined) {
        return NotificationService.vueToastificationInstance.error(content, options);
    }
    public [TYPE.WARNING](content: ToastContent, options?: (ToastOptions & {type?: TYPE.WARNING | undefined}) | undefined) {
        return NotificationService.vueToastificationInstance.warning(content, options);
    }
}

export const Notification = NotificationService.Instance();