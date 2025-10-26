<template>
  <div class="products py-12 md:py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold mb-4 gradient-text font-bengali">আমাদের পণ্যসমূহ</h1>
        <p class="text-gray-600 text-lg font-bengali">তাজা ও মানসম্মত কৃষিপণ্য</p>
      </div>

      <!-- Category Filter -->
      <div class="flex flex-wrap justify-center gap-4 mb-12">
        <button 
          @click="selectedCategory = null"
          :class="selectedCategory === null ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          সকল পণ্য
        </button>
        <button 
          @click="selectedCategory = 'fish'"
          :class="selectedCategory === 'fish' ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          🐟 মাছ
        </button>
        <button 
          @click="selectedCategory = 'dairy'"
          :class="selectedCategory === 'dairy' ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          🐄 দুগ্ধজাত
        </button>
        <button 
          @click="selectedCategory = 'poultry'"
          :class="selectedCategory === 'poultry' ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          🐔 মুরগি
        </button>
        <button 
          @click="selectedCategory = 'crops'"
          :class="selectedCategory === 'crops' ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          🌾 ফসল
        </button>
        <button 
          @click="selectedCategory = 'fruits'"
          :class="selectedCategory === 'fruits' ? 'btn-primary' : 'bg-white text-gray-700 border-2 border-gray-300 px-6 py-3 rounded-lg hover:border-primary-600 hover:text-primary-600 transition-all font-bengali font-medium'"
        >
          🥭 ফল
        </button>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-primary-600"></div>
        <p class="mt-4 text-gray-600 font-bengali">লোড হচ্ছে...</p>
      </div>

      <!-- Products Grid -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <div 
          v-for="product in filteredProducts" 
          :key="product.id"
          class="card group hover:-translate-y-2 transition-all duration-300"
        >
          <!-- Product Image -->
          <div class="relative overflow-hidden h-56">
            <img 
              :src="product.image" 
              :alt="product.name_bn"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
            />
            <div v-if="product.price" class="absolute top-4 right-4 bg-primary-600 text-white px-4 py-2 rounded-full font-bold shadow-lg">
              ৳{{ product.price }}
            </div>
          </div>

          <!-- Product Info -->
          <div class="p-6">
            <h3 class="text-xl font-bold mb-2 font-bengali text-gray-800">{{ product.name_bn }}</h3>
            <p class="text-gray-600 mb-4 font-bengali text-sm">{{ product.description_bn }}</p>
            
            <div class="flex flex-wrap gap-2">
              <a 
                href="tel:+8801711727357"
                class="flex-1 text-center bg-primary-600 text-white px-4 py-2 rounded-lg hover:bg-primary-700 transition-colors font-bengali text-sm font-medium"
              >
                অর্ডার করুন
              </a>
              <button 
                @click="showDetails(product)"
                class="flex-1 text-center bg-gray-200 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-300 transition-colors font-bengali text-sm font-medium"
              >
                বিস্তারিত
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="!loading && filteredProducts.length === 0" class="text-center py-12">
        <div class="text-6xl mb-4">📦</div>
        <p class="text-gray-600 text-lg font-bengali">এই বিভাগে কোনো পণ্য নেই</p>
      </div>
    </div>

    <!-- Product Detail Modal -->
    <transition name="fade">
      <div 
        v-if="selectedProduct" 
        @click="selectedProduct = null"
        class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4"
      >
        <div 
          @click.stop
          class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl"
        >
          <div class="relative">
            <img 
              :src="selectedProduct.image" 
              :alt="selectedProduct.name_bn"
              class="w-full h-64 md:h-96 object-cover"
            />
            <button 
              @click="selectedProduct = null"
              class="absolute top-4 right-4 bg-white text-gray-700 w-10 h-10 rounded-full shadow-lg hover:bg-gray-100 transition-colors"
            >
              ✕
            </button>
          </div>
          
          <div class="p-8">
            <h2 class="text-3xl font-bold mb-4 font-bengali text-gray-800">{{ selectedProduct.name_bn }}</h2>
            <p class="text-gray-600 mb-6 font-bengali leading-relaxed">{{ selectedProduct.description_bn }}</p>
            
            <div v-if="selectedProduct.price" class="mb-6">
              <div class="flex items-center justify-between bg-gray-50 p-4 rounded-lg">
                <span class="text-gray-700 font-bengali font-medium">মূল্য:</span>
                <span class="text-3xl font-bold text-primary-600">৳{{ selectedProduct.price }}</span>
              </div>
            </div>

            <div class="flex gap-4">
              <a 
                href="tel:+8801711727357"
                class="flex-1 text-center btn-primary"
              >
                📞 এখনই অর্ডার করুন
              </a>
              <a 
                href="mailto:nishat@manishatagro.com"
                class="flex-1 text-center bg-gray-200 text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-300 transition-colors font-bengali font-medium"
              >
                📧 ইমেইল করুন
              </a>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Products',
  data() {
    return {
      products: [],
      selectedCategory: null,
      loading: true,
      selectedProduct: null
    }
  },
  computed: {
    filteredProducts() {
      if (!this.selectedCategory) {
        return this.products
      }
      return this.products.filter(p => p.category === this.selectedCategory)
    }
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('/api/products')
        this.products = response.data
      } catch (error) {
        console.error('Error fetching products:', error)
      } finally {
        this.loading = false
      }
    },
    showDetails(product) {
      this.selectedProduct = product
    }
  },
  mounted() {
    this.fetchProducts()
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
