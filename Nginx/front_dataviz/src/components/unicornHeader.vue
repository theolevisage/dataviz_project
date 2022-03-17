<template>
    <nav class="flex items-center justify-between flex-wrap bg-pink-400 p-6">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
            <svg style="width:28px;height:28px" viewBox="0 0 24 24">
                <path fill="currentColor" d="M20 12V19L17 20L14 15.33C13.71 14.89 13 15.14 13.08 15.67L14 23L4 18L4.96 12.75C5.56 9.42 8.46 7 11.84 7H13L19 1L17 7H20L18.42 9.37C19.36 9.88 20 10.86 20 12Z" />
            </svg>
            <span class="ml-2 font-semibold text-xl tracking-tight">Licornes en loc'</span>
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
                <a @click="goto('/')" class="block mt-4 lg:inline-block lg:mt-0 text-pink-200 hover:text-white mr-4">
                    Accueil
                </a>
                <a @click="goto('/contact')" class="block mt-4 lg:inline-block lg:mt-0 text-pink-200 hover:text-white mr-4">
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