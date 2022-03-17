<template>
    <nav class="flex items-center justify-between flex-wrap bg-teal-400 p-6">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M4.626 8.878a7.937 7.937 0 0 1 1.71-2.541 7.92 7.92 0 0 1 2.542-1.71 8.12 8.12 0 0 1 6.13-.041A2.49 2.49 0 0 0 17.5 7C18.886 7 20 5.886 20 4.5S18.886 2 17.5 2c-.689 0-1.312.276-1.763.725-2.431-.973-5.223-.958-7.635.059-1.19.5-2.26 1.22-3.18 2.139A9.98 9.98 0 0 0 2 12h2c0-1.086.211-2.136.626-3.122zm14.747 6.244c-.401.952-.977 1.808-1.71 2.541s-1.589 1.309-2.542 1.71a8.12 8.12 0 0 1-6.13.041A2.488 2.488 0 0 0 6.5 17C5.114 17 4 18.114 4 19.5S5.114 22 6.5 22c.689 0 1.312-.276 1.763-.725A9.973 9.973 0 0 0 12 22a9.983 9.983 0 0 0 9.217-6.102A9.992 9.992 0 0 0 22 12h-2a7.993 7.993 0 0 1-.627 3.122z"></path><path d="M12 7.462c-2.502 0-4.538 2.036-4.538 4.538S9.498 16.538 12 16.538c2.502 0 4.538-2.036 4.538-4.538S14.502 7.462 12 7.462z"></path></svg>
            <span class="ml-2 font-semibold text-xl tracking-tight">DATAVIZ'</span>
        </div>
        <div class="block lg:hidden">
            <button @click="toggleCollapse" class="flex items-center px-3 py-2 border rounded text-pink-200 border-pink-200 hover:text-white hover:border-white">
                <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <title>Menu</title>
                    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                </svg>
            </button>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto" v-show="!collapse">
            <div class="text-sm lg:flex-grow">
                <a @click="goto('/')" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Accueil
                </a>
                <a @click="goto('/contact')" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Contact
                </a>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "header",
        data() {
            return {
                windowWidth: window.innerWidth,
                collapse: false
            }
        },
        methods: {
            toggleCollapse() {
                this.collapse = !this.collapse;
            },
            onResize() {
                this.windowWidth = window.innerWidth
            },
            goto(route) {
                this.$router.push(route);
            }
        },
        watch: {
            windowWidth(newHeight, oldHeight) {
                console.log(`it changed to ${newHeight} from ${oldHeight}`);
                if(newHeight < 1024) {
                    this.collapse = true;
                }else{
                    this.collapse = false;
                }
            }
        },
        mounted() {
            this.$nextTick(() => {
                window.addEventListener('resize', this.onResize);
            })
        },
        beforeDestroy() {
            window.removeEventListener('resize', this.onResize);
        }
    }
</script>

<style scoped>

</style>