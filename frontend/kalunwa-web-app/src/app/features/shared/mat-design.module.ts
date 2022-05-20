import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatCardModule} from '@angular/material/card';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';
import {MatChipsModule} from '@angular/material/chips';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatDialogModule} from '@angular/material/dialog';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import { NgImageSliderModule } from 'ng-image-slider';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';

const MATERIAL = [
  MatToolbarModule,
  MatButtonModule,
  MatMenuModule,
  MatIconModule,
  MatSidenavModule,
  MatCardModule,
  MatButtonToggleModule,
  MatPaginatorModule,
  MatChipsModule,
  MatAutocompleteModule,
  MatDialogModule,
  MatInputModule,
  MatSelectModule,
  NgImageSliderModule,
  MatProgressSpinnerModule
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
