import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatCardModule} from '@angular/material/card';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
<<<<<<< HEAD
import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';
import {MatChipsModule} from '@angular/material/chips';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatDialogModule} from '@angular/material/dialog';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import { NgImageSliderModule } from 'ng-image-slider';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
=======
>>>>>>> f7d4bc3e457799addec5e273255ce9282c64d29b

const MATERIAL = [
  MatToolbarModule,
  MatButtonModule,
  MatMenuModule,
  MatIconModule,
  MatSidenavModule,
  MatCardModule,
<<<<<<< HEAD
  MatButtonToggleModule,
  MatPaginatorModule,
  MatChipsModule,
  MatAutocompleteModule,
  MatDialogModule,
  MatInputModule,
  MatSelectModule,
  NgImageSliderModule,
  MatProgressSpinnerModule
=======
  MatButtonToggleModule
>>>>>>> f7d4bc3e457799addec5e273255ce9282c64d29b
];

@NgModule({
  declarations: [],
  exports: [MATERIAL],
  imports: [
    CommonModule,
    MATERIAL
  ]
})
export class MatDesignModule { }
